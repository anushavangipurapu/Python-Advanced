
import csv
import logging
import time

from celery import Task, shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import transaction
from django.template.loader import render_to_string

from employees.models import Employee, Notification

logger = logging.getLogger(__name__)


class LoggingTask(Task):
    abstract = True

    def __call__(self, *args, **kwargs):
        started_at = time.monotonic()
        task_id = self.request.id

        logger.info(
            "Task started: task=%s task_id=%s",
            self.name,
            task_id,
        )

        try:
            result = super().__call__(*args, **kwargs)
        except Exception:
            duration = time.monotonic() - started_at

            logger.exception(
                "Task failed: task=%s task_id=%s duration_seconds=%.3f",
                self.name,
                task_id,
                duration,
            )
            raise

        duration = time.monotonic() - started_at

        logger.info(
            "Task finished: task=%s task_id=%s duration_seconds=%.3f",
            self.name,
            task_id,
            duration,
        )

        return result
@shared_task(
    bind=True,
    base=LoggingTask,
    name="employees.send_welcome_email",
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_backoff_max=60,
    retry_jitter=True,
    retry_kwargs={"max_retries": 3},
    soft_time_limit=30,
    time_limit=40,
)
def send_welcome_email(self, employee_id):
    """
    Send a welcome email to an employee.

    Uses the employee ID so the task can reload fresh database data.
    Avoids sending another welcome email when it is already marked sent.
    """

    with transaction.atomic():
        employee = Employee.objects.get(pk=employee_id)

        recipient_email = employee.email

        if not recipient_email:
            raise ValueError("Employee recipient email is missing.")

        try:
            validate_email(recipient_email)
        except ValidationError as exc:
            raise ValueError(
                "Invalid employee recipient email."
            ) from exc

        notification, created = Notification.objects.get_or_create(
            employee=employee,
            notification_type="WELCOME",
            defaults={
                "subject": "Welcome to Employee Management",
                "message": (
                    f"Welcome {employee.first_name} "
                    f"{employee.last_name}!"
                ),
                "recipient_email": recipient_email,
                "email_sent": False,
            },
        )

        notification = (
            Notification.objects.select_for_update()
            .get(pk=notification.pk)
        )

        if notification.email_sent:
            return f"Welcome email already sent for employee {employee_id}"

        html_message = render_to_string(
            "emails/welcome_email.html",
            {"employee": employee},
        )

        email = EmailMultiAlternatives(
            subject=notification.subject,
            body=notification.message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[notification.recipient_email],
        )

        email.attach_alternative(html_message, "text/html")

        email.send(fail_silently=False)

        notification.email_sent = True
        notification.email_error = ""
        notification.save(
            update_fields=["email_sent", "email_error"]
        )

    return f"Welcome email sent for employee {employee_id}"
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
        logger.exception("Employee report task failed")
        raise


@shared_task
def process_employee_csv(file_path):
    logger.info("CSV processing task started: file_path=%s", file_path)

    try:
        created = 0
        skipped = 0
        failed = 0
        errors = []

        with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            required_columns = {"first_name", "last_name", "email"}

            if not required_columns.issubset(reader.fieldnames or []):
                raise ValueError("CSV is missing required columns")

            for row_number, row in enumerate(reader, start=2):
                try:
                    email = row["email"].strip()

                    if not email:
                        failed += 1
                        errors.append(f"Row {row_number}: email is required")
                        continue

                    if Employee.objects.filter(email=email).exists():
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
                    errors.append(f"Row {row_number}: {str(exc)}")

        logger.info(
            "CSV processing completed: created=%s skipped=%s failed=%s",
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
        logger.exception("CSV processing task failed: file_path=%s", file_path)
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

        checked_count = Employee.objects.filter(is_active=False).count()
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