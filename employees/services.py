import csv
from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError
from django.db import transaction

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
        employee.save(
            update_fields=["department", "updated_at"]
        )

        # 10. Return transfer record
        return transfer


REQUIRED_COLUMNS = {
    "employee_code",
    "first_name",
    "last_name",
    "email",
    "phone",
    "department",
    "designation",
    "salary",
    "joining_date",
    "role",
    "is_active",
}


class EmployeeCSVImportService:

    @staticmethod
    @transaction.atomic
    def import_csv(file_path):
        created = 0
        skipped = 0
        failed = 0
        errors = []

        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8-sig",
        ) as file:

            reader = csv.DictReader(file)

            if not reader.fieldnames:
                raise ValidationError(
                    "CSV file is empty."
                )

            missing_columns = (
                REQUIRED_COLUMNS - set(reader.fieldnames)
            )

            if missing_columns:
                raise ValidationError(
                    "Missing required columns: "
                    + ", ".join(sorted(missing_columns))
                )

            for row_number, row in enumerate(
                reader,
                start=2,
            ):
                try:
                    required_row_fields = [
                        "employee_code",
                        "first_name",
                        "last_name",
                        "email",
                        "phone",
                        "department",
                        "designation",
                        "salary",
                        "joining_date",
                        "role",
                        "is_active",
                    ]

                    missing_values = [
                        field
                        for field in required_row_fields
                        if not row.get(field)
                    ]

                    if missing_values:
                        raise ValidationError(
                            "Missing values: "
                            + ", ".join(missing_values)
                        )

                    employee_code = row[
                        "employee_code"
                    ].strip()

                    email = row[
                        "email"
                    ].strip()

                    salary = Decimal(
                        row["salary"].strip()
                    )

                    if not employee_code or not email:
                        raise ValidationError(
                            "Employee code and email are required."
                        )

                    # Check duplicate employee code
                    if Employee.objects.filter(
                        employee_code=employee_code
                    ).exists():
                        skipped += 1
                        continue

                    # Check duplicate email
                    if Employee.objects.filter(
                        email=email
                    ).exists():
                        skipped += 1
                        continue

                    # Find department
                    department = Department.objects.filter(
                        name=row["department"].strip()
                    ).first()

                    if not department:
                        raise ValidationError(
                            f"Department "
                            f"'{row['department']}' not found."
                        )

                    # Create employee object
                    employee = Employee(
                        employee_code=employee_code,
                        first_name=row[
                            "first_name"
                        ].strip(),
                        last_name=row[
                            "last_name"
                        ].strip(),
                        email=email,
                        phone=row[
                            "phone"
                        ].strip(),
                        department=department,
                        designation=row[
                            "designation"
                        ].strip(),
                        salary=salary,
                        joining_date=row[
                            "joining_date"
                        ].strip(),
                        role=row[
                            "role"
                        ].strip(),
                        is_active=row[
                            "is_active"
                        ].strip().lower()
                        in ["true", "1", "yes"],
                    )

                    # Validate employee before saving
                    employee.full_clean()

                    # Save employee
                    employee.save()

                    created += 1

                except (
                    ValidationError,
                    ValueError,
                    InvalidOperation,
                ) as exc:

                    failed += 1

                    errors.append(
                        f"Row {row_number}: {exc}"
                    )

        return {
            "created": created,
            "skipped": skipped,
            "failed": failed,
            "errors": errors,
        }