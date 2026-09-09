from django.http import JsonResponse
from .models import Employee


def health_check(request):
    return JsonResponse({
        "status": "success",
        "message": "Employee Management Backend is running"
    })


def employee_list(request):
    employees = Employee.objects.all()

    return JsonResponse({
        "status": "success",
        "employees": [
            {
                "id": employee.id,
                "employee_code": employee.employee_code,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "email": employee.email,
                "phone": employee.phone,
                "department": employee.department,
                "designation": employee.designation,
                "salary": str(employee.salary),
                "joining_date": str(employee.joining_date),
                "is_active": employee.is_active,
            }
            for employee in employees
        ]
    })


def employee_detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Employee not found"
        }, status=404)

    return JsonResponse({
        "id": employee.id,
        "employee_code": employee.employee_code,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "email": employee.email,
        "phone": employee.phone,
        "department": employee.department,
        "designation": employee.designation,
        "salary": str(employee.salary),
        "joining_date": str(employee.joining_date),
        "is_active": employee.is_active,
    })