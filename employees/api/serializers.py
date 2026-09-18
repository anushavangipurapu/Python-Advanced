from datetime import date
import re

from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee

        fields = [
            "id",
            "employee_code",
            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "designation",
            "salary",
            "joining_date",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_employee_code(self, value):
        if not value.startswith("EMP"):
            raise serializers.ValidationError(
                "Employee code must start with EMP."
            )

        if not value[3:].isdigit():
            raise serializers.ValidationError(
                "Employee code must contain numbers after EMP."
            )

        employee_id = self.instance.id if self.instance else None

        if Employee.objects.exclude(id=employee_id).filter(
            employee_code=value
        ).exists():
            raise serializers.ValidationError(
                "Employee code already exists."
            )

        return value

    def validate_email(self, value):
        employee_id = self.instance.id if self.instance else None

        if Employee.objects.exclude(id=employee_id).filter(
            email=value
        ).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Salary cannot be negative."
            )

        if value > 10000000:
            raise serializers.ValidationError(
                "Salary cannot exceed 10000000."
            )

        return value

    def validate_joining_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Joining date cannot be in the future."
            )

        return value

    def validate_phone(self, value):
        if not re.fullmatch(r"\d{10}", str(value)):
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value