from django.contrib import admin
from .models import Employee, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "is_active",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_code",
        "first_name",
        "last_name",
        "email",
        "department",
        "designation",
        "salary",
        "is_active",
    )

    search_fields = (
        "employee_code",
        "first_name",
        "last_name",
        "email",
    )

    list_filter = (
        "department",
        "is_active",
    )

    ordering = (
        "employee_code",
    )