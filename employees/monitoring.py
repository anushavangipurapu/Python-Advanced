import logging
import time

import redis
from celery import current_app
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)

MONITORED_QUEUES = [
    "default",
    "reports",
    "maintenance",
    "notifications",
]

QUEUE_DEPTH_WARNING = 100
TASK_AGE_WARNING_SECONDS = 300


def get_monitoring_snapshot():
    """Return a best-effort snapshot of Celery and Redis health."""
    snapshot = {
        "timestamp": time.time(),
        "redis": {"status": "unknown"},
        "workers": {"status": "unknown"},
        "queues": {},
        "tasks": {"active": 0, "reserved": 0},
        "alerts": [],
        "limitations": [],
    }

    # Check Redis broker and queue depth.
    try:
        client = redis.Redis.from_url(
            settings.CELERY_BROKER_URL,
            socket_connect_timeout=2,
            socket_timeout=2,
        )
        client.ping()
        snapshot["redis"] = {"status": "healthy"}

        for queue_name in MONITORED_QUEUES:
            depth = client.llen(queue_name)
            snapshot["queues"][queue_name] = {
                "depth": depth,
                "status": (
                    "warning"
                    if depth >= QUEUE_DEPTH_WARNING
                    else "ok"
                ),
            }

            if depth >= QUEUE_DEPTH_WARNING:
                snapshot["alerts"].append(
                    f"Queue backlog warning: {queue_name}, depth={depth}"
                )

    except Exception:
        logger.exception("Celery broker health check failed.")
        snapshot["redis"] = {"status": "unavailable"}
        snapshot["alerts"].append(
            "Celery broker Redis is unavailable."
        )

    # Inspect Celery workers and tasks.
    try:
        inspector = current_app.control.inspect(timeout=2)
        ping_result = inspector.ping() or {}
        active_result = inspector.active() or {}
        reserved_result = inspector.reserved() or {}

        if ping_result:
            snapshot["workers"] = {
                "status": "healthy",
                "count": len(ping_result),
                "names": list(ping_result.keys()),
            }
        else:
            snapshot["workers"] = {
                "status": "unavailable",
                "count": 0,
                "names": [],
            }
            snapshot["alerts"].append(
                "No Celery workers responded to ping."
            )

        snapshot["tasks"] = {
            "active": sum(
                len(items) for items in active_result.values()
            ),
            "reserved": sum(
                len(items) for items in reserved_result.values()
            ),
        }

    except Exception:
        logger.exception("Celery worker inspection failed.")
        snapshot["workers"] = {
            "status": "inspection_error",
            "count": 0,
            "names": [],
        }
        snapshot["alerts"].append(
            "Could not inspect Celery workers."
        )

    # Check Django cache.
    try:
        cache_key = "day4_monitoring_health_check"
        cache.set(cache_key, "ok", timeout=10)
        healthy = cache.get(cache_key) == "ok"
        cache.delete(cache_key)

        snapshot["cache"] = {
            "status": "healthy" if healthy else "unhealthy"
        }

        if not healthy:
            snapshot["alerts"].append(
                "Django cache read/write health check failed."
            )

    except Exception:
        logger.exception("Django cache health check failed.")
        snapshot["cache"] = {"status": "unavailable"}
        snapshot["alerts"].append(
            "Django cache is unavailable."
        )

    # Read cache metrics.
    try:
        from employees.cache_services import get_cache_metrics

        snapshot["cache_metrics"] = get_cache_metrics()
    except Exception:
        logger.exception("Could not read cache metrics.")
        snapshot["cache_metrics"] = {
            "hits": 0,
            "misses": 0,
            "errors": 0,
        }
        snapshot["alerts"].append(
            "Could not read cache hit/miss metrics."
        )

    # Read task metrics.
    try:
        from employees.monitoring_metrics import get_task_metrics

        snapshot["task_metrics"] = get_task_metrics()
    except Exception:
        logger.exception("Could not read task metrics.")
        snapshot["task_metrics"] = {
            "success": 0,
            "failure": 0,
            "retry": 0,
        }
        snapshot["alerts"].append(
            "Could not read task metrics."
        )

    snapshot["limitations"] = [
        "Queue depth measures waiting messages, not active tasks.",
        "Queue names must match the configured broker transport.",
        "Success, failure and retry rates require task event or "
        "persistent result tracking.",
        "Cache hit/miss rates require explicit instrumentation.",
        "Task age is not reported because reliable start timestamps "
        "are not available from every worker inspection response.",
    ]

    return snapshot
