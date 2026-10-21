
import logging
import time

from django.core.cache import cache
from django.db.models import Count, Q
from django_redis import get_redis_connection

from employees.models import Department

logger = logging.getLogger(__name__)

DEPARTMENT_STATS_CACHE_KEY = "department_employee_stats_v1"
DEPARTMENT_STATS_CACHE_TIMEOUT = 300
DEPARTMENT_STATS_LOCK_KEY = "department_employee_stats_lock_v1"
DEPARTMENT_STATS_LOCK_TIMEOUT = 15
DEPARTMENT_STATS_LOCK_WAIT_SECONDS = 2


def _fetch_department_employee_stats():
    """Fetch department statistics from the database."""
    return list(
        Department.objects.annotate(
            total_employees=Count("employees"),
            active_employees=Count(
                "employees",
                filter=Q(employees__is_active=True),
            ),
            inactive_employees=Count(
                "employees",
                filter=Q(employees__is_active=False),
            ),
        )
        .values(
            "id",
            "name",
            "code",
            "total_employees",
            "active_employees",
            "inactive_employees",
        )
        .order_by("name")
    )


def get_department_employee_stats():
    """Return cached statistics, using a Redis lock to reduce cache stampedes."""
    try:
        cached_stats = cache.get(DEPARTMENT_STATS_CACHE_KEY)
    except Exception:
        logger.exception("Cache read failed; fetching statistics from the database.")
        return _fetch_department_employee_stats()

    if cached_stats is not None:
        return cached_stats

    lock = None

    try:
        redis_client = get_redis_connection("default")
        lock = redis_client.lock(
            DEPARTMENT_STATS_LOCK_KEY,
            timeout=DEPARTMENT_STATS_LOCK_TIMEOUT,
            blocking_timeout=DEPARTMENT_STATS_LOCK_WAIT_SECONDS,
        )

        acquired = lock.acquire(blocking=True)
    except Exception:
        logger.exception("Cache lock unavailable; fetching statistics from the database.")
        return _fetch_department_employee_stats()

    if not acquired:
        # Another request may be populating the cache.
        try:
            cached_stats = cache.get(DEPARTMENT_STATS_CACHE_KEY)
            if cached_stats is not None:
                return cached_stats
        except Exception:
            logger.exception("Cache recheck failed after lock timeout.")

        # Bounded fallback: don't wait indefinitely.
        return _fetch_department_employee_stats()

    try:
        # Double-check after acquiring the lock.
        try:
            cached_stats = cache.get(DEPARTMENT_STATS_CACHE_KEY)
        except Exception:
            logger.exception("Cache recheck failed; fetching statistics from the database.")
            return _fetch_department_employee_stats()

        if cached_stats is not None:
            return cached_stats

        stats = _fetch_department_employee_stats()

        try:
            cache.set(
                DEPARTMENT_STATS_CACHE_KEY,
                stats,
                timeout=DEPARTMENT_STATS_CACHE_TIMEOUT,
            )
        except Exception:
            logger.exception("Cache write failed; returning database results.")

        return stats
    finally:
        try:
            lock.release()
        except Exception:
            logger.warning("Could not release department statistics cache lock.", exc_info=True)


def invalidate_department_employee_stats():
    """Remove cached department statistics after employee changes."""
    try:
        cache.delete(DEPARTMENT_STATS_CACHE_KEY)
    except Exception:
        logger.exception("Cache invalidation failed.")
