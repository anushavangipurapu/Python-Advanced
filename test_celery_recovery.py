
from celery import Celery

app = Celery(
    "recovery_test",
    broker="memory://",
    backend="cache+memory://",
)

app.conf.task_always_eager = True
app.conf.task_eager_propagates = False


@app.task(
    bind=True,
    autoretry_for=(ValueError,),
    retry_backoff=True,
    retry_backoff_max=2,
    retry_jitter=False,
    max_retries=3,
    name="recovery_test.retry_task",
)
def retry_task(self):
    attempt = self.request.retries + 1
    print(f"Attempt {attempt}")

    if attempt <= 2:
        raise ValueError("Intentional temporary failure")

    return "Success after retries"


if __name__ == "__main__":
    result = retry_task.apply()

    print("Final state:", result.state)
    print("Final result:", repr(result.result))

    if result.successful() and result.result == "Success after retries":
        print("PASS: Task recovered after retry attempts.")
    else:
        print("FAIL: Task did not recover as expected.")
