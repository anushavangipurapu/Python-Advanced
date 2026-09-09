from django.http import JsonResponse


employees_data = [
    {
        "id": 1,
        "name": "Divya",
        "department": "Backend",
        "designation": "Python Developer",
    },
    {
        "id": 2,
        "name": "Anusha",
        "department": "Frontend",
        "designation": "React Developer",
    },
    {
        "id": 3,
        "name": "Rahul",
        "department": "Testing",
        "designation": "QA Engineer",
    },
]


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
            return JsonResponse({
                "employee": employee
            })

    return JsonResponse({
        "status": "error",
        "message": "Employee not found"
    }, status=404)