from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from employees.models import Employee

from .serializers import EmployeeSerializer


class EmployeeListCreateView(ListCreateAPIView):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer
    