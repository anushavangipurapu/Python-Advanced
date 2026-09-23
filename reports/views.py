from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Avg, Max, Min, Sum
from employees.models import Department, Project, Employee


@api_view(["GET"])
def department_summary(request):
    departments = Department.objects.annotate(
        employee_count=Count("employees"),
        average_salary=Avg("employees__salary"),
        maximum_salary=Max("employees__salary")
    )

    data = []

    for department in departments:
        data.append({
            "department": department.name,
            "employee_count": department.employee_count,
            "average_salary": department.average_salary,
            "maximum_salary": department.maximum_salary,
        })

    return Response(data)


@api_view(["GET"])
def project_summary(request):
    projects = Project.objects.annotate(
        employee_count=Count("employees", distinct=True)
    )

    data = []

    for project in projects:
        data.append({
            "project": project.name,
            "project_code": project.project_code,
            "employee_count": project.employee_count,
        })

    return Response(data)


@api_view(["GET"])
def salary_summary(request):
    report = Employee.objects.aggregate(
        total_employees=Count("id"),
        average_salary=Avg("salary"),
        maximum_salary=Max("salary"),
        minimum_salary=Min("salary"),
        total_salary=Sum("salary"),
    )

    return Response(report)
