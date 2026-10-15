
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


app.conf.timezone = "UTC"
app.conf.enable_utc = True

app.conf.beat_schedule = {}


