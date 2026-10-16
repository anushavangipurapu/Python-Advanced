
from celery import Celery

app = Celery(
    "duplicate_test",
    broker="memory://",
    backend="cache+memory://",
)

app.conf.task_always_eager = True

# In-memory store for this isolated demonstration
processed_keys = set()
side_effects = []


@app.task(name="duplicate_test.process_operation")
def process_operation(operation_id):
    if operation_id in processed_keys:
        print(f"Duplicate prevented: {operation_id}")
        return "already processed"

    # Simulate one side effect without touching the database or email
    processed_keys.add(operation_id)
    side_effects.append(operation_id)

    print(f"Operation processed: {operation_id}")
    return "processed"


if __name__ == "__main__":
    operation_id = "demo-operation-001"

    first = process_operation.apply(args=[operation_id])
    second = process_operation.apply(args=[operation_id])

    print("First result:", first.result)
    print("Second result:", second.result)
    print("Side-effect count:", len(side_effects))

    assert len(side_effects) == 1
    print("PASS: Duplicate operation did not repeat the simulated side effect.")
