import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    name="employees.recovery_test_failure",
    max_retries=3,
    default_retry_delay=2,
)
def recovery_test_failure(self):
    attempt = self.request.retries + 1

    logger.warning(
        "Recovery test attempt %s; task_id=%s",
        attempt,
        self.request.id,
    )

    try:
        raise ValueError("Intentional recovery demo failure")
    except ValueError as exc:
        raise self.retry(exc=exc, countdown=2)