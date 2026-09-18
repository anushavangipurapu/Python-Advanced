from django.http import Http404

from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee

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