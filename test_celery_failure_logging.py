import logging
import time

from celery import Celery, Task

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s %(message)s",
)


class LoggingTask(Task):
    abstract = True

    def __call__(self, *args, **kwargs):
        started_at = time.monotonic()
        task_id = self.request.id

        logging.info(
            "Task started: task=%s task_id=%s",
            self.name,
            task_id,
        )

        try:
            result = super().__call__(*args, **kwargs)
        except Exception:
            duration = time.monotonic() - started_at
            logging.exception(
                "Task failed: task=%s task_id=%s duration_seconds=%.3f",
                self.name,
                task_id,
                duration,
            )
            raise

        duration = time.monotonic() - started_at
        logging.info(
            "Task finished: task=%s task_id=%s duration_seconds=%.3f",
            self.name,
            task_id,
            duration,
        )
        return result


app = Celery(
    "failure_logging_test",
    broker="memory://",
    backend="cache+memory://",
)


@app.task(
    bind=True,
    base=LoggingTask,
    name="demo.failure_logging",
)
def demo_failure(self):
    raise ValueError("Intentional test failure")


if __name__ == "__main__":
    result = demo_failure.apply(
        task_id="failure-log-test-001",
        throw=False,
    )

    if result.failed():
        print("PASS: Failure logging test completed.")
        print("Expected exception:", type(result.result).__name__)
    else:
        print("FAIL: The task did not fail as expected.")
