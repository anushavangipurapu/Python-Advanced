
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
