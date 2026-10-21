
from functools import wraps

from django_redis import get_redis_connection


def prevent_overlap(lock_name, timeout=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            redis_client = get_redis_connection("default")
            lock = redis_client.lock(
                lock_name,
                timeout=timeout,
                blocking=False,
            )

            acquired = lock.acquire(blocking=False)

            if not acquired:
                print(
                    f"Skipping {func.__name__}: "
                    "another execution is in progress."
                )
                return None

            try:
                return func(*args, **kwargs)
            finally:
                try:
                    lock.release()
                except Exception as exc:
                    print(f"Could not release lock {lock_name}: {exc}")

        return wrapper

    return decorator
