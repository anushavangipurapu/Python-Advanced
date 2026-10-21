
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "employee_management.settings",
)

django.setup()

from django_redis import get_redis_connection
from employees.task_utils import prevent_overlap

redis_client = get_redis_connection("default")

lock = redis_client.lock(
    "celery:test:overlap",
    timeout=60,
    blocking=False,
)

acquired = lock.acquire(blocking=False)
print("Test lock acquired:", acquired)


@prevent_overlap("celery:test:overlap", timeout=60)
def dummy_task():
    print("ERROR: duplicate execution occurred")
    return "executed"


try:
    if acquired:
        result = dummy_task()
        print("Second execution result:", result)
finally:
    if acquired:
        lock.release()
