from django.http import Http404

from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee, EmployeeTransfer
from employees.services import EmployeeTransferService

from .serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):

    queryset = Employee.objects.all().order_by("id")

    serializer_class = EmployeeSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        "first_name",
        "last_name",
        "email",
        "employee_code",
        "department",
    ]

    ordering_fields = [
        "salary",
        "joining_date",
    ]

    def get_queryset(self):
        queryset = Employee.objects.all().order_by("id")

        department = self.request.query_params.get("department")
        is_active = self.request.query_params.get("is_active")
        salary_min = self.request.query_params.get("salary_min")

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

    def destroy(self, request, *args, **kwargs):
        try:
            employee = self.get_object()
        except Http404:
            return Response(
                {"detail": "Employee not found."},
                status=404,
            )

        employee.delete()

        return Response(status=204)

    @action(detail=False, methods=["get"])
    def active(self, request):
        employees = Employee.objects.filter(
            is_active=True
        ).order_by("id")

        serializer = self.get_serializer(
            employees,
            many=True
        )

        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path="transfer")
    def transfer(self, request, pk=None):
        to_department_id = request.data.get("to_department")
        reason = request.data.get("reason")

        if not to_department_id:
            return Response(
                {"detail": "Target department is required."},
                status=400,
            )

        if not reason:
            return Response(
                {"detail": "Transfer reason is required."},
                status=400,
            )

        try:
            transfer = EmployeeTransferService.transfer_employee(
                employee_id=pk,
                to_department_id=to_department_id,
                reason=reason,
                transferred_by=(
                    request.user
                    if request.user.is_authenticated
                    else None
                ),
            )
        except Exception as exc:
            return Response(
                {"detail": str(exc)},
                status=400,
            )

        return Response(
            {
                "message": "Employee transferred successfully.",
                "transfer_id": transfer.id,
                "employee_id": transfer.employee_id,
                "from_department": transfer.from_department.name,
                "to_department": transfer.to_department.name,
                "reason": transfer.reason,
                "status": transfer.status,
            },
            status=200,
        )

    @action(
        detail=True,
        methods=["get"],
        url_path="transfer-history"
    )
    def transfer_history(self, request, pk=None):
        try:
            employee = self.get_object()
        except Http404:
            return Response(
                {"detail": "Employee not found."},
                status=404,
            )

        history = EmployeeTransfer.objects.filter(
            employee=employee
        ).select_related(
            "from_department",
            "to_department",
            "transferred_by"
        ).order_by("-transferred_at")

        data = []

        for transfer in history:
            data.append(
                {
                    "id": transfer.id,
                    "from_department": transfer.from_department.name,
                    "to_department": transfer.to_department.name,
                    "reason": transfer.reason,
                    "status": transfer.status,
                    "transferred_at": transfer.transferred_at,
                }
            )

        return Response(
            {
                "employee_id": employee.id,
                "employee_name": str(employee),
                "transfer_history": data,
            }
        )