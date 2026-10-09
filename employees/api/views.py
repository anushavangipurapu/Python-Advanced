from django.http import Http404
from django.utils import timezone
from rest_framework.decorators import action, api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from employees.tasks import send_welcome_email
from employees.cache_services import invalidate_department_employee_stats
from employees.cache_services import get_department_employee_stats
from employees.models import (
    Employee,
    EmployeeTransfer,
    Notification,
)

from employees.permissions import (
    IsAdmin,
    IsHR,
    IsManager,
    IsEmployee,
)

from employees.services import EmployeeTransferService

from .serializers import (
    EmployeeSerializer,
    NotificationSerializer,
)


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        "first_name",
        "last_name",
        "email",
        "employee_code",
        "department__name",
    ]

    ordering_fields = [
        "salary",
        "joining_date",
    ]

    def get_permissions(self):
        # Create: ADMIN and HR only
        if self.action == "create":
            permission_classes = [IsAdmin | IsHR]

        # Update: ADMIN, HR, and EMPLOYEE
        # EMPLOYEE can update only their own record
        elif self.action in ["update", "partial_update"]:
            permission_classes = [
                IsAdmin | IsHR | IsEmployee
            ]

        # Delete: ADMIN only
        elif self.action == "destroy":
            permission_classes = [IsAdmin]

        # Transfer: ADMIN, HR, and MANAGER
        elif self.action == "transfer":
            permission_classes = [
                IsAdmin | IsHR | IsManager
            ]

        # Transfer history: all authenticated roles
        elif self.action == "transfer_history":
            permission_classes = [
                IsAdmin | IsHR | IsManager | IsEmployee
            ]

        # List, retrieve, and active: all roles
        elif self.action in ["list", "retrieve", "active"]:
            permission_classes = [
                IsAdmin | IsHR | IsManager | IsEmployee
            ]

        else:
            permission_classes = [
                IsAdmin | IsHR | IsManager | IsEmployee
            ]

        return [
            permission_class()
            for permission_class in permission_classes
        ]
    def perform_create(self, serializer):
        serializer.save()
        invalidate_department_employee_stats()

    def perform_update(self, serializer):
        serializer.save()
        invalidate_department_employee_stats()

    def perform_destroy(self, instance):
        instance.delete()
        invalidate_department_employee_stats()
    def get_queryset(self):
        queryset = Employee.objects.all().order_by("id")

        # EMPLOYEE can access only their own Employee record
        if (
            self.request.user.is_authenticated
            and hasattr(
                self.request.user,
                "employee_profile",
            )
            and self.request.user.employee_profile.role
            == "EMPLOYEE"
        ):
            queryset = queryset.filter(
                user=self.request.user
            )

        department = self.request.query_params.get(
            "department"
        )
        is_active = self.request.query_params.get(
            "is_active"
        )
        salary_min = self.request.query_params.get(
            "salary_min"
        )

        if department:
            queryset = queryset.filter(
                department=department
            )

        if is_active:
            queryset = queryset.filter(
                is_active=is_active.lower() == "true"
            )

        if salary_min:
            queryset = queryset.filter(
                salary__gte=salary_min
            )

        return queryset

    def retrieve(self, request, *args, **kwargs):
        try:
            employee = self.get_object()
        except Http404:
            return Response(
                {"detail": "Employee not found."},
                status=404,
            )

        serializer = self.get_serializer(employee)

        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        try:
            employee = self.get_object()
        except Http404:
            return Response(
                {"detail": "Employee not found."},
                status=404,
            )

        serializer = self.get_serializer(employee)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            employee = self.get_object()
        except Http404:
            return Response(
                {"detail": "Employee not found."},
                status=404,
            )

        self.perform_destroy(employee)
        return Response(status=204)
    def transfer(self, request, pk=None):
        to_department_id = request.data.get(
            "to_department"
        )
        reason = request.data.get("reason")

        if not to_department_id:
            return Response(
                {
                    "detail": (
                        "Target department is required."
                    )
                },
                status=400,
            )

        if not reason:
            return Response(
                {
                    "detail": (
                        "Transfer reason is required."
                    )
                },
                status=400,
            )

        try:
            transfer = (
                EmployeeTransferService.transfer_employee(
                    employee_id=pk,
                    to_department_id=to_department_id,
                    reason=reason,
                    transferred_by=(
                        request.user
                        if request.user.is_authenticated
                        else None
                    ),
                )
            )

        except Exception as exc:
            return Response(
                {"detail": str(exc)},
                status=400,
            )
        invalidate_department_employee_stats()
        return Response(
            {
                "message": (
                    "Employee transferred successfully."
                ),
                "transfer_id": transfer.id,
                "employee_id": transfer.employee_id,
                "from_department": (
                    transfer.from_department.name
                ),
                "to_department": (
                    transfer.to_department.name
                ),
                "reason": transfer.reason,
                "status": transfer.status,
            },
            status=200,
        )

    @action(
        detail=True,
        methods=["get"],
        url_path="transfer-history",
    )
    def transfer_history(self, request, pk=None):
        try:
            employee = self.get_object()
        except Http404:
            return Response(
                {"detail": "Employee not found."},
                status=404,
            )

        history = (
            EmployeeTransfer.objects.filter(
                employee=employee
            )
            .select_related(
                "from_department",
                "to_department",
                "transferred_by",
            )
            .order_by("-transferred_at")
        )

        data = []

        for transfer in history:
            data.append(
                {
                    "id": transfer.id,
                    "from_department": (
                        transfer.from_department.name
                    ),
                    "to_department": (
                        transfer.to_department.name
                    ),
                    "reason": transfer.reason,
                    "status": transfer.status,
                    "transferred_at": (
                        transfer.transferred_at
                    ),
                }
            )

        return Response(
            {
                "employee_id": employee.id,
                "employee_name": str(employee),
                "transfer_history": data,
            }
        )


class MyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            employee = request.user.employee_profile
        except Employee.DoesNotExist:
            return Response(
                {
                    "detail": (
                        "Employee profile not found."
                    )
                },
                status=404,
            )

        serializer = EmployeeSerializer(employee)

        return Response(
            serializer.data,
            status=200,
        )

    def patch(self, request):
        try:
            employee = request.user.employee_profile
        except Employee.DoesNotExist:
            return Response(
                {
                    "detail": (
                        "Employee profile not found."
                    )
                },
                status=404,
            )

        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=200,
            )

        return Response(
            serializer.errors,
            status=400,
        )


class EmployeeProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {
                    "detail": (
                        "Employee profile not found."
                    )
                },
                status=404,
            )

        user_employee = request.user.employee_profile
        role = user_employee.role

        # Employee can access only own profile
        if (
            role == "EMPLOYEE"
            and employee.id != user_employee.id
        ):
            return Response(
                {
                    "detail": (
                        "You are not authorized "
                        "to access this profile."
                    )
                },
                status=403,
            )

        # Manager can access only own profile
        if (
            role == "MANAGER"
            and employee.id != user_employee.id
        ):
            return Response(
                {
                    "detail": (
                        "You are not authorized "
                        "to access this profile."
                    )
                },
                status=403,
            )

        # HR and Admin can access employee profiles
        serializer = EmployeeSerializer(employee)

        return Response(
            serializer.data,
            status=200,
        )

    def patch(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {
                    "detail": (
                        "Employee profile not found."
                    )
                },
                status=404,
            )

        user_employee = request.user.employee_profile
        role = user_employee.role

        # Employee can update only own profile
        if (
            role == "EMPLOYEE"
            and employee.id != user_employee.id
        ):
            return Response(
                {
                    "detail": (
                        "You are not authorized "
                        "to update this profile."
                    )
                },
                status=403,
            )

        # Only Admin, HR and Employee can update profiles
        if role not in [
            "ADMIN",
            "HR",
            "EMPLOYEE",
        ]:
            return Response(
                {
                    "detail": (
                        "You are not authorized "
                        "to update this profile."
                    )
                },
                status=403,
            )

        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=200,
            )

        return Response(
            serializer.errors,
            status=400,
        )


class NotificationListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            employee = request.user.employee_profile
        except Employee.DoesNotExist:
            return Response(
                {
                    "detail": (
                        "Employee profile not found."
                    )
                },
                status=404,
            )

        notifications = (
            Notification.objects.filter(
                employee=employee
            )
            .order_by("-created_at")
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return Response(
            serializer.data,
            status=200,
        )
class NotificationListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            employee = request.user.employee_profile
        except Employee.DoesNotExist:
            return Response(
                {
                    "detail": "Employee profile not found."
                },
                status=404,
            )

        notifications = (
            Notification.objects.filter(
                employee=employee
            )
            .order_by("-created_at")
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return Response(
            serializer.data,
            status=200,
        )
class NotificationMarkReadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            employee = request.user.employee_profile
        except Employee.DoesNotExist:
            return Response(
                {
                    "detail": "Employee profile not found."
                },
                status=404,
            )

        try:
            notification = Notification.objects.get(
                pk=pk,
                employee=employee,
            )
        except Notification.DoesNotExist:
            return Response(
                {
                    "detail": "Notification not found."
                },
                status=404,
            )

        notification.is_read = True
        notification.read_at = timezone.now()

        notification.save(
            update_fields=[
                "is_read",
                "read_at",
            ]
        )

        serializer = NotificationSerializer(
            notification
        )

        return Response(
            serializer.data,
            status=200,
        )
class DepartmentEmployeeStatsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stats = get_department_employee_stats()
        return Response(stats)
