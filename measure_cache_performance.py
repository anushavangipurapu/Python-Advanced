
import os
import statistics
import time

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "employee_management.settings",
)

import django
django.setup()

from django.core.cache import cache
from employees.cache_services import (
    DEPARTMENT_STATS_CACHE_KEY,
    get_department_employee_stats,
)


def measure_cache_off(iterations=10):
    timings = []

    for _ in range(iterations):
        cache.delete(DEPARTMENT_STATS_CACHE_KEY)

        start = time.perf_counter()
        get_department_employee_stats()
        elapsed = time.perf_counter() - start

        timings.append(elapsed * 1000)

    return timings


def measure_cache_on(iterations=10):
    timings = []

    get_department_employee_stats()

    for _ in range(iterations):
        start = time.perf_counter()
        get_department_employee_stats()
        elapsed = time.perf_counter() - start

        timings.append(elapsed * 1000)

    return timings


def show_results(label, timings):
    print(f"\n{label}")
    print(f"Average: {statistics.mean(timings):.2f} ms")
    print(f"Minimum: {min(timings):.2f} ms")
    print(f"Maximum: {max(timings):.2f} ms")


if __name__ == "__main__":
    print("Department Statistics Cache Performance Test")
    print("Iterations: 10")

    cache_off_times = measure_cache_off()
    cache_on_times = measure_cache_on()

    show_results("Cache OFF (database query)", cache_off_times)
    show_results("Cache ON (cached result)", cache_on_times)
