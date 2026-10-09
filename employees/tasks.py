import csv
import logging

from celery import shared_task

from employees.models import Employee
from employees.services import NotificationService


logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_backoff_max=60,
    retry_jitter=True,
    retry_kwargs={"max_retries": 3},
)
def send_welcome_email(self, employee_id):
    logger.info(
        "Welcome email task started: employee_id=%s",
        employee_id,
    )

    try:
        employee = Employee.objects.get(id=employee_id)

        NotificationService.send_welcome_notification(employee)

        logger.info(
            "Welcome email task completed: employee_id=%s",
            employee_id,
        )

        return {
            "status": "success",
            "employee_id": employee_id,
            "message": "Welcome email processed successfully",
        }

    except Exception:
        logger.exception(
            "Welcome email task failed: employee_id=%s",
            employee_id,
        )
        raise


@shared_task
def generate_employee_report():
    logger.info("Employee report task started")

    try:
        employees = Employee.objects.filter(
            is_active=True
        ).values(
            "id",
            "first_name",
            "last_name",
            "email",
            "department_id",
        )

        report = list(employees)

        logger.info(
            "Employee report task completed: employee_count=%s",
            len(report),
        )

        return {
            "status": "success",
            "employee_count": len(report),
            "employees": report,
        }

    except Exception:
        logger.exception(
            "Employee report task failed"
        )
        raise


@shared_task
def process_employee_csv(file_path):
    logger.info(
        "CSV processing task started: file_path=%s",
        file_path,
    )

    try:
        created = 0
        skipped = 0
        failed = 0
        errors = []

        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8",
        ) as csv_file:
            reader = csv.DictReader(csv_file)

            required_columns = {
                "first_name",
                "last_name",
                "email",
            }

            if not required_columns.issubset(
                reader.fieldnames or []
            ):
                raise ValueError(
                    "CSV is missing required columns"
                )

            for row_number, row in enumerate(
                reader,
                start=2,
            ):
                try:
                    email = row["email"].strip()

                    if not email:
                        failed += 1
                        errors.append(
                            f"Row {row_number}: email is required"
                        )
                        continue

                    if Employee.objects.filter(
                        email=email
                    ).exists():
                        skipped += 1
                        continue

                    Employee.objects.create(
                        first_name=row["first_name"].strip(),
                        last_name=row["last_name"].strip(),
                        email=email,
                    )

                    created += 1

                except Exception as exc:
                    failed += 1
                    errors.append(
                        f"Row {row_number}: {str(exc)}"
                    )

        logger.info(
            "CSV processing task completed: "
            "created=%s skipped=%s failed=%s",
            created,
            skipped,
            failed,
        )

        return {
            "status": "completed",
            "created": created,
            "skipped": skipped,
            "failed": failed,
            "errors": errors,
        }

    except Exception:
        logger.exception(
            "CSV processing task failed: file_path=%s",
            file_path,
        )
        raise
@shared_task
def deactivate_inactive_employees():
    """Deactivate linked user accounts for inactive employees."""
    logger.info("Inactive employee maintenance task started")

    try:
        inactive_employees = Employee.objects.filter(
            is_active=False,
            user__is_active=True,
        ).select_related("user")

        checked_count = Employee.objects.filter(
            is_active=False,
        ).count()

        deactivated_count = 0

        for employee in inactive_employees:
            employee.user.is_active = False
            employee.user.save(update_fields=["is_active"])
            deactivated_count += 1

        logger.info(
            "Inactive employee maintenance completed: "
            "inactive_employees=%s, accounts_deactivated=%s",
            checked_count,
            deactivated_count,
        )

        return {
            "status": "success",
            "inactive_employees": checked_count,
            "accounts_deactivated": deactivated_count,
        }

    except Exception:
        logger.exception("Inactive employee maintenance task failed")
        raise
