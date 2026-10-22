
import logging

import redis
from celery.signals import task_failure, task_retry, task_success
from django.conf import settings

logger = logging.getLogger(__name__)

METRICS_KEY = "employee_management:celery:task_metrics"


def _record_metric(metric_name):
    """Increment a shared Redis counter for a Celery task event."""
    try:
        client = redis.Redis.from_url(
            settings.CELERY_BROKER_URL,
            socket_connect_timeout=2,
            socket_timeout=2,
        )
        client.hincrby(METRICS_KEY, metric_name, 1)
    except Exception:
        logger.exception("Could not record Celery metric: %s", metric_name)


@task_success.connect
def record_task_success(sender=None, **kwargs):
    _record_metric("success")


@task_failure.connect
def record_task_failure(sender=None, **kwargs):
    _record_metric("failure")


@task_retry.connect
def record_task_retry(sender=None, **kwargs):
    _record_metric("retry")



def get_task_metrics():
    """Return shared task counters from Redis."""
    try:
        client = redis.Redis.from_url(
            settings.CELERY_BROKER_URL,
            socket_connect_timeout=2,
            socket_timeout=2,
        )
        values = client.hgetall(METRICS_KEY)

        return {
            "success": int(values.get(b"success", 0)),
            "failure": int(values.get(b"failure", 0)),
            "retry": int(values.get(b"retry", 0)),
        }
    except Exception:
        logger.exception("Could not read Celery task metrics.")
        return {
            "success": 0,
            "failure": 0,
            "retry": 0,
        }
