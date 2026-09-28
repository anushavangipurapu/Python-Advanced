from django.db import transaction
from django.core.exceptions import ValidationError

from .models import Employee, Department, EmployeeTransfer


class EmployeeTransferService:

    @staticmethod
    @transaction.atomic
    def transfer_employee(
        employee_id,
        to_department_id,
        reason,
        transferred_by=None,
    ):
        # 1. Find employee
        try:
            employee = Employee.objects.select_for_update().get(
                id=employee_id
            )
        except Employee.DoesNotExist:
            raise ValidationError("Employee not found.")

        # 2. Verify employee is active
        if not employee.is_active:
            raise ValidationError("Employee is inactive.")

        # 3. Find target department
        try:
            to_department = Department.objects.get(
                id=to_department_id
            )
        except Department.DoesNotExist:
            raise ValidationError("Target department not found.")

        # 4. Verify target department is active
        if not to_department.is_active:
            raise ValidationError("Target department is inactive.")

        # 5. Verify target department is different
        if employee.department_id == to_department.id:
            raise ValidationError(
                "Employee is already in this department."
            )

        # 6. Verify reason
        if not reason or not reason.strip():
            raise ValidationError("Transfer reason is required.")

        # 7. Store current department
        from_department = employee.department

        # 8. Create transfer history
        transfer = EmployeeTransfer.objects.create(
            employee=employee,
            from_department=from_department,
            to_department=to_department,
            reason=reason,
            transferred_by=transferred_by,
            status="COMPLETED",
        )

        # 9. Update employee department
        employee.department = to_department
        employee.save(update_fields=["department", "updated_at"])

        # 10. Return transfer record
        return transfer