
import logging

from django.core.cache import cache
from django.db.models import Count, Q

from employees.models import Department

logger = logging.getLogger(__name__)

DEPARTMENT_STATS_CACHE_KEY = "department_employee_stats_v1"
DEPARTMENT_STATS_CACHE_TIMEOUT = 300


def get_department_employee_stats():
    """Return cached department statistics, falling back to the database."""
    try:
        cached_stats = cache.get(DEPARTMENT_STATS_CACHE_KEY)
    except Exception:
        logger.exception("Cache read failed; fetching department statistics from the database.")
        cached_stats = None

    if cached_stats is not None:
        return cached_stats

    stats = list(
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

    try:
        cache.set(
            DEPARTMENT_STATS_CACHE_KEY,
            stats,
            timeout=DEPARTMENT_STATS_CACHE_TIMEOUT,
        )
    except Exception:
        logger.exception("Cache write failed; returning database results.")

    return stats


def invalidate_department_employee_stats():
    """Remove cached department statistics after employee changes."""
    try:
        cache.delete(DEPARTMENT_STATS_CACHE_KEY)
    except Exception:
        logger.exception("Cache invalidation failed.")
