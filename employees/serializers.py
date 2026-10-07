from rest_framework import serializers

from .models import Employee, Notification


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_employee_code(self, value):
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

        return value
        class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            "id",
            "employee",
            "notification_type",
            "subject",
            "message",
            "recipient_email",
            "is_read",
            "email_sent",
            "email_error",
            "created_at",
            "read_at",
        ]
        read_only_fields = [
            "id",
            "notification_type",
            "subject",
            "message",
            "recipient_email",
            "email_sent",
            "email_error",
            "created_at",
            "read_at",
        ]