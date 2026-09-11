import json
import logging

from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Employee


logger = logging.getLogger("employees")


def employee_to_dict(employee):
    return {
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


def health_check(request):
    logger.info("Health check endpoint called")

    return JsonResponse({
        "status": "success",
        "message": "Employee Management Backend is running"
    })


@csrf_exempt
def employee_list(request):
    if request.method == "GET":
        department = request.GET.get("department")

        if department:
            employees = Employee.objects.filter(
                department=department
            )
        else:
            employees = Employee.objects.all()

        return JsonResponse({
            "status": "success",
            "employees": [
                employee_to_dict(employee)
                for employee in employees
            ]
        })

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            required_fields = [
                "employee_code",
                "first_name",
                "last_name",
                "email",
                "phone",
                "department",
                "designation",
                "salary",
                "joining_date",
            ]

            for field in required_fields:
                if field not in data or data[field] in ["", None]:
                    return JsonResponse({
                        "status": "error",
                        "message": f"{field} is required"
                    }, status=400)

            if Employee.objects.filter(
                employee_code=data["employee_code"]
            ).exists():
                return JsonResponse({
                    "status": "error",
                    "message": "Employee code already exists"
                }, status=400)

            if Employee.objects.filter(
                email=data["email"]
            ).exists():
                return JsonResponse({
                    "status": "error",
                    "message": "Email already exists"
                }, status=400)

            if float(data["salary"]) < 0:
                return JsonResponse({
                    "status": "error",
                    "message": "Salary cannot be negative"
                }, status=400)

            employee = Employee.objects.create(
                employee_code=data["employee_code"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                phone=data["phone"],
                department=data["department"],
                designation=data["designation"],
                salary=data["salary"],
                joining_date=data["joining_date"],
                is_active=data.get("is_active", True),
            )

            logger.info(
                "Employee created successfully: %s",
                employee.employee_code
            )

            return JsonResponse({
                "status": "success",
                "message": "Employee created successfully",
                "employee": employee_to_dict(employee)
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON"
            }, status=400)

        except ValueError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid salary"
            }, status=400)

    return JsonResponse({
        "status": "error",
        "message": "Method not allowed"
    }, status=405)


@csrf_exempt
def employee_detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Employee not found"
        }, status=404)

    if request.method == "GET":
        return JsonResponse(employee_to_dict(employee))

    if request.method in ["PUT", "PATCH"]:
        try:
            data = json.loads(request.body)

            if "email" in data:
                if Employee.objects.filter(
                    email=data["email"]
                ).exclude(id=id).exists():
                    return JsonResponse({
                        "status": "error",
                        "message": "Email already exists"
                    }, status=400)

                employee.email = data["email"]

            if "employee_code" in data:
                if Employee.objects.filter(
                    employee_code=data["employee_code"]
                ).exclude(id=id).exists():
                    return JsonResponse({
                        "status": "error",
                        "message": "Employee code already exists"
                    }, status=400)

                employee.employee_code = data["employee_code"]

            fields = [
                "first_name",
                "last_name",
                "phone",
                "department",
                "designation",
                "salary",
                "joining_date",
                "is_active",
            ]

            for field in fields:
                if field in data:
                    setattr(employee, field, data[field])

            if employee.salary < 0:
                return JsonResponse({
                    "status": "error",
                    "message": "Salary cannot be negative"
                }, status=400)

            employee.save()

            logger.info(
                "Employee updated successfully: %s",
                employee.employee_code
            )

            return JsonResponse({
                "status": "success",
                "message": "Employee updated successfully"
            })

        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON"
            }, status=400)

    if request.method == "DELETE":
        employee_code = employee.employee_code
        employee.delete()

        logger.info(
            "Employee deleted successfully: %s",
            employee_code
        )

        return JsonResponse({
            "status": "success",
            "message": "Employee deleted successfully"
        })

    return JsonResponse({
        "status": "error",
        "message": "Method not allowed"
    }, status=405)


def invalid_redirect(request):
    return redirect("employee-list")