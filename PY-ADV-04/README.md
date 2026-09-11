
27-Aug-2026

## Objective

To understand Python performance, optimization, memory usage,
multithreading, multiprocessing, GIL, and asynchronous programming.

---

# 1. PYTHON EXECUTION PERFORMANCE

## Definition




## Syntax

```python
print("Program started")

# Python code

print("Program finished")
````

## Program

```python
print("Program started")

for i in range(5):
    print(i)

print("Program finished")
```

## Output

```text
Program started
0
1
2
3
4
Program finished
```

---

# 2. IDENTIFY INEFFICIENT CODE

## Definition

Inefficient code is code that takes more time or memory than necessary.



## Syntax

```python
for item in items:
    # process item
```

## Program

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print("Original numbers:", numbers)
print("Result:", result)
```

## Output

```text
Original numbers: [1, 2, 3, 4, 5]
Result: [2, 4, 6, 8, 10]
```

---

# 3. USE TIMEIT

## Definition

`timeit` is a Python module used to measure how much time a piece
of code takes to execute.



## Syntax

```python
import timeit

time_taken = timeit.timeit(
    "code",
    number=n
)
```

## Program

```python
import timeit

time_taken = timeit.timeit(
    "sum(range(1000))",
    number=10000
)

print("Code: sum(range(1000))")
print("Number of executions: 10000")
print("Time taken:", time_taken, "seconds")
```

## Output

```text
Code: sum(range(1000))
Number of executions: 10000
Time taken: approximately 0.2 seconds
```

---

# 4. ANALYZE MEMORY USAGE

## Definition

Memory analysis means checking how much memory a Python object uses.



## Syntax

```python
import sys

sys.getsizeof(object)
```

## Program

```python
import sys

numbers = [1, 2, 3, 4, 5]

memory_used = sys.getsizeof(numbers)

print("Numbers:", numbers)
print("Memory used by list:", memory_used, "bytes")
```

## Output

```text
Numbers: [1, 2, 3, 4, 5]
Memory used by list: 104 bytes
```

---

# 5. OPTIMIZE LOOPS AND DATA PROCESSING

## Definition

Optimization means improving code so that it can perform work
more efficiently.



## Syntax

### Normal loop

```python
result = []

for item in items:
    result.append(expression)
```

### List comprehension

```python
result = [expression for item in items]
```

## Program

```python
numbers = []

for i in range(10):
    numbers.append(i * 2)

print("Using normal loop:", numbers)

optimized_numbers = [i * 2 for i in range(10)]

print("Using list comprehension:", optimized_numbers)
```

## Output

```text
Using normal loop: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
Using list comprehension: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

# 6. COMPARE LIST VS GENERATOR APPROACHES

## Definition

A list stores all values in memory.

A generator produces values one at a time when they are needed.



## Syntax

### List

```python
my_list = [x for x in range(n)]
```

### Generator

```python
my_generator = (x for x in range(n))
```

## Program

```python
import sys

my_list = [x for x in range(100000)]

my_generator = (x for x in range(100000))

print("List memory:", sys.getsizeof(my_list), "bytes")
print("Generator memory:", sys.getsizeof(my_generator), "bytes")
```

## Output

```text
List memory: 800984 bytes
Generator memory: 192 bytes
```

Values may vary depending on the Python version/system.

---

# 7. UNDERSTAND MULTIPROCESSING

## Definition

Multiprocessing means using multiple processes to perform work.

It is useful for CPU-intensive tasks.

S
## Syntax

```python
import multiprocessing

process = multiprocessing.Process(
    target=function,
    args=(value,)
)

process.start()
process.join()
```

## Program

```python
import multiprocessing


def worker(number):
    print("Process is working on:", number, flush=True)


if __name__ == "__main__":

    process1 = multiprocessing.Process(
        target=worker,
        args=(1,)
    )

    process2 = multiprocessing.Process(
        target=worker,
        args=(2,)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processes completed")
```

## Output

```text
Process is working on: 1
Process is working on: 2
All processes completed
```

Order may change.

---

# 8. UNDERSTAND MULTITHREADING

## Definition

Multithreading means using multiple threads within a program
to perform tasks concurrently.


## Syntax

```python
import threading

thread = threading.Thread(
    target=function,
    args=(value,)
)

thread.start()
thread.join()
```

## Program

```python
import threading
import time


def worker(name):
    print(name, "started")

    time.sleep(2)

    print(name, "finished")


thread1 = threading.Thread(
    target=worker,
    args=("Thread 1",)
)

thread2 = threading.Thread(
    target=worker,
    args=("Thread 2",)
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads completed")
```

## Output

```text
Thread 1 started
Thread 2 started
Thread 1 finished
Thread 2 finished
All threads completed
```

---

# 9. UNDERSTAND PYTHON GIL

## Definition

GIL stands for Global Interpreter Lock.

In CPython, the GIL allows only one thread at a time to execute
Python bytecode.



## Syntax

```python
import threading

thread = threading.Thread(target=function)

thread.start()
thread.join()
```

## Program

```python
import threading


def cpu_task():
    total = 0

    for i in range(10_000_000):
        total = total + i

    print("CPU task completed")


thread1 = threading.Thread(target=cpu_task)
thread2 = threading.Thread(target=cpu_task)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads completed")
```

## Output

```text
CPU task completed
CPU task completed
Both threads completed
```

## Important Point

```text
I/O-bound work  → Threading can help
CPU-bound work  → Multiprocessing can help
```

---

# 10. IMPLEMENT A MULTITHREADING EXAMPLE

## Definition

A multithreading example uses multiple threads to perform
multiple tasks concurrently.


## Syntax

```python
thread = threading.Thread(
    target=function,
    args=(value,)
)

thread.start()
thread.join()
```

## Program

```python
import threading
import time


def download_file(file_name):
    print("Starting:", file_name)

    time.sleep(2)

    print("Finished:", file_name)


start_time = time.time()

thread1 = threading.Thread(
    target=download_file,
    args=("File 1",)
)

thread2 = threading.Thread(
    target=download_file,
    args=("File 2",)
)

thread3 = threading.Thread(
    target=download_file,
    args=("File 3",)
)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

end_time = time.time()

print("Total time:", end_time - start_time, "seconds")
```

## Output

```text
Starting: File 1
Starting: File 2
Starting: File 3
Finished: File 1
Finished: File 3
Finished: File 2
Total time: approximately 2 seconds
```

---

# 11. MULTIPROCESSING FOR CPU-INTENSIVE WORK

## Definition

CPU-intensive work requires a lot of CPU calculation.

Multiprocessing can divide CPU-intensive work among multiple processes.



## Syntax

```python
with multiprocessing.Pool(processes=n) as pool:
    results = pool.map(function, data)
```

## Program

```python
import multiprocessing
import time


def calculate_square(number):
    total = 0

    for i in range(1_000_000):
        total += number * number

    return total


if __name__ == "__main__":

    numbers = [10, 20, 30, 40]

    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(calculate_square, numbers)

    end_time = time.time()

    print("Results:", results)
    print("Number of processes:", 4)
    print("Time taken:", end_time - start_time, "seconds")
```

## Output

```text
Results: [100000000, 400000000, 900000000, 1600000000]
Number of processes: 4
Time taken: approximately 5.93 seconds
```

---

# 12. ASYNCHRONOUS PROGRAMMING USING ASYNCIO

## Definition

Asynchronous programming allows a program to work on other tasks
while waiting for an operation to complete.



## Syntax

```python
import asyncio

async def function():
    await asyncio.sleep(seconds)

asyncio.run(function())
```

## Program

```python
import asyncio


async def task(name):
    print(name, "started")

    await asyncio.sleep(2)

    print(name, "finished")


async def main():

    await asyncio.gather(
        task("Async Task 1"),
        task("Async Task 2"),
        task("Async Task 3")
    )


asyncio.run(main())
```

## Output

```text
Async Task 1 started
Async Task 2 started
Async Task 3 started
Async Task 1 finished
Async Task 2 finished
Async Task 3 finished
```

---

# 13. CREATE ASYNCHRONOUS TASKS

## Definition

An asynchronous task is a scheduled coroutine that can run
through the asyncio event loop.



## Syntax

```python
task = asyncio.create_task(function())
```

## Program

```python
import asyncio


async def download_data(name, seconds):
    print(name, "started")

    await asyncio.sleep(seconds)

    print(name, "finished")

    return name + " completed"


async def main():

    task1 = asyncio.create_task(
        download_data("Task 1", 2)
    )

    task2 = asyncio.create_task(
        download_data("Task 2", 3)
    )

    task3 = asyncio.create_task(
        download_data("Task 3", 1)
    )

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1)
    print(result2)
    print(result3)


asyncio.run(main())
```

## Output

```text
Task 1 started
Task 2 started
Task 3 started
Task 3 finished
Task 1 finished
Task 2 finished
Task 1 completed
Task 2 completed
Task 3 completed
```

---

# 14. SYNCHRONOUS VS ASYNCHRONOUS EXECUTION

## Definition

Synchronous execution runs tasks one after another.

Asynchronous execution allows waiting tasks to make progress
without blocking the event loop.



## Syntax

### Synchronous

```python
function1()
function2()
function3()
```

### Asynchronous

```python
await asyncio.gather(
    function1(),
    function2(),
    function3()
)
```

## Program

```python
import asyncio
import time


def synchronous_task(name):
    print(name, "started")

    time.sleep(2)

    print(name, "finished")


async def asynchronous_task(name):
    print(name, "started")

    await asyncio.sleep(2)

    print(name, "finished")


print("----- SYNCHRONOUS EXECUTION -----")

start_time = time.time()

synchronous_task("Sync Task 1")
synchronous_task("Sync Task 2")
synchronous_task("Sync Task 3")

sync_time = time.time() - start_time

print("Synchronous time:", sync_time, "seconds")


print("----- ASYNCHRONOUS EXECUTION -----")


async def run_async_tasks():

    start_time = time.time()

    await asyncio.gather(
        asynchronous_task("Async Task 1"),
        asynchronous_task("Async Task 2"),
        asynchronous_task("Async Task 3")
    )

    async_time = time.time() - start_time

    print("Asynchronous time:", async_time, "seconds")


asyncio.run(run_async_tasks())
```

## Output

```text
Synchronous time: approximately 6 seconds
Asynchronous time: approximately 2 seconds
```

---

# 15. BENCHMARK THE IMPLEMENTATIONS

## Definition

Benchmarking means measuring and comparing the performance of
different implementations.



## Syntax

```python
start = time.time()

# code

end = time.time()

print(end - start)
```

## Program

```python
import time
import threading
import asyncio


def sync_work():
    time.sleep(2)
    time.sleep(2)
    time.sleep(2)


def thread_work():
    time.sleep(2)


def run_threads():

    thread1 = threading.Thread(target=thread_work)
    thread2 = threading.Thread(target=thread_work)
    thread3 = threading.Thread(target=thread_work)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


async def run_async():

    await asyncio.gather(
        asyncio.sleep(2),
        asyncio.sleep(2),
        asyncio.sleep(2)
    )


start = time.time()
sync_work()
sync_time = time.time() - start


start = time.time()
run_threads()
thread_time = time.time() - start


start = time.time()
asyncio.run(run_async())
async_time = time.time() - start


print("Synchronous time:", sync_time, "seconds")
print("Multithreading time:", thread_time, "seconds")
print("Async time:", async_time, "seconds")
```

## Actual Benchmark Result

```text
Synchronous time: 6.001 seconds
Multithreading time: 2.002 seconds
Async time: 2.005 seconds
```

---

# 16. DOCUMENT PERFORMANCE DIFFERENCES

## Definition

Performance documentation means recording and explaining the
performance differences between different approaches.



## Performance Table

| Implementation |          Time |
| -------------- | ------------: |
| Synchronous    | 6.001 seconds |
| Multithreading | 2.002 seconds |
| Asynchronous   | 2.005 seconds |

## Analysis

### Synchronous

Tasks are executed one by one.

```text
Task 1 → Task 2 → Task 3
```

Time: approximately 6 seconds.

### Multithreading

Multiple I/O-bound tasks can progress concurrently.

```text
Thread 1 ─┐
Thread 2 ─┼→ approximately 2 seconds
Thread 3 ─┘
```

### Asynchronous

Async tasks can make progress while waiting.

```text
Async Task 1 ─┐
Async Task 2 ─┼→ approximately 2 seconds
Async Task 3 ─┘
```

### Multiprocessing

Multiple processes can be used for CPU-intensive work.

### Generator

Generators can reduce memory usage for large sequences because
values are produced when needed.

---

# DELIVERABLES

## 1. Synchronous Implementation

Completed successfully.

## 2. Multithreaded Implementation

Completed successfully.

## 3. Multiprocessing Implementation

Completed successfully.

## 4. Async Implementation

Completed successfully using `asyncio`.

## 5. Benchmark Report

Completed successfully.

Benchmark:

```text
Synchronous       : 6.001 seconds
Multithreading    : 2.002 seconds
Asynchronous      : 2.005 seconds
```

---

# EVALUATION

## Performance Understanding — 25%

Understood:

* Execution time
* Memory usage
* `timeit`
* Benchmarking
* Optimization

## Async Programming — 25%

Understood:

* `async`
* `await`
* `asyncio`
* `asyncio.run()`
* `asyncio.gather()`
* `asyncio.create_task()`

## Threading / Multiprocessing — 20%

Understood:

* Threads
* Processes
* Thread creation
* Process creation
* CPU-bound work
* I/O-bound work

## Optimization — 20%

Understood:

* Loop optimization
* List comprehension
* Generators
* Memory efficiency
* Performance measurement

## Technical Explanation — 10%

Understood:

* Python GIL
* Threading vs multiprocessing
* Synchronous vs asynchronous execution
* CPU-bound vs I/O-bound tasks
* Performance benchmarking

---

# FINAL CONCLUSION

Python performance can be improved by choosing the correct approach
for the type of work.

```text
CPU-bound work
       ↓
Multiprocessing

I/O-bound work
       ↓
Multithreading / Async

Large data
       ↓
Generators

Performance measurement
       ↓
timeit / Benchmarking
```

