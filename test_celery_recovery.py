
import logging

from celery import Celery, Task

logging.basicConfig(level=logging.INFO)

app = Celery(
    "recovery_test",
    broker="memory://",
    backend="cache+memory://",
)

app.conf.task_always_eager = True
app.conf.task_eager_propagates = False


class RetryTestTask(Task):
    abstract = True
    autoretry_for = (ValueError,)
    retry_backoff = True
    retry_backoff_max = 2
    retry_jitter = False
    max_retries = 3


@app.task(
    bind=True,
    base=RetryTestTask,
    name="recovery_test.retry_task",
)
def retry_task(self):
    attempt = self.request.retries + 1
    print(f"Attempt {attempt}: intentional test failure")
    raise ValueError("Intentional recovery test failure")


if __name__ == "__main__":
    result = retry_task.apply()
    print("Final state:", result.state)
    print("Final result:", repr(result.result))
    print("Retries configured: 3")
