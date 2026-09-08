from django.http import JsonResponse


employees_data = []


def health_check(request):
    return JsonResponse({
        "status": "success",
        "message": "Employee Management Backend is running"
    })


def employee_list(request):
    return JsonResponse({
        "status": "success",
        "employees": employees_data
    })


def employee_detail(request, id):
    for employee in employees_data:
        if employee["id"] == id:
            return JsonResponse(employee)

    return JsonResponse({
        "status": "error",
        "message": "Employee not found"
    }, status=404)