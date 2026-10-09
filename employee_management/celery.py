
import os

from celery import Celery


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "employee_management.settings",
)

app = Celery("employee_management")

app.config_from_object(
    "django.conf:settings",
    namespace="CELERY",
)

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "daily-employee-report": {
        "task": "employees.tasks.generate_employee_report",
        "schedule": 60.0 * 60 * 24,
    },
    "inactive-employee-maintenance": {
        "task": "employees.tasks.deactivate_inactive_employees",
        "schedule": 60.0 * 60 * 24,
    },
}
