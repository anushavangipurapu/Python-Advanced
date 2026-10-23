
import os
import time

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "employee_management.settings",
)

import django
django.setup()

from employee_management.celery import app
from employees.tasks import generate_employee_report


if __name__ == "__main__":
    result = generate_employee_report.apply_async(
        queue="reports",
        expires=1,
    )

    print("Task ID:", result.id)
    print("Queue: reports")
    print("Expiry configured: 1 second")

    time.sleep(2)

    print(
        "PASS: Expiry-configured task was published."
    )
    print(
        "Note: Broker-side expiration still needs "
        "verification using worker/broker evidence."
    )
