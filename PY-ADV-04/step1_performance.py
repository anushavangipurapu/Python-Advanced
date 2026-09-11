# ============================================================
# PY-ADV-04 — Python Performance, Multithreading & Async
# ============================================================


# ============================================================
# 1. UNDERSTAND PYTHON EXECUTION PERFORMANCE
# ============================================================

print("========================================")
print("1. PYTHON EXECUTION PERFORMANCE")
print("========================================")

print("Program started")

for i in range(5):
    print(i)

print("Program finished")
# ============================================================
# 2. IDENTIFY INEFFICIENT CODE
# ============================================================

print()
print("========================================")
print("2. IDENTIFY INEFFICIENT CODE")
print("========================================")

numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print("Original numbers:", numbers)
print("Result:", result)
# ============================================================
# 3. USE TIMEIT
# ============================================================

print()
print("========================================")
print("3. USE TIMEIT")
print("========================================")

import timeit

time_taken = timeit.timeit(
    "sum(range(1000))",
    number=10000
)

print("Code: sum(range(1000))")
print("Number of executions: 10000")
print("Time taken:", time_taken, "seconds")
# ============================================================
# 4. ANALYZE MEMORY USAGE
# ============================================================

print()
print("========================================")
print("4. ANALYZE MEMORY USAGE")
print("========================================")

import sys

numbers = [1, 2, 3, 4, 5]

memory_used = sys.getsizeof(numbers)

print("Numbers:", numbers)
print("Memory used by list:", memory_used, "bytes")
# ============================================================
# 5. OPTIMIZE LOOPS AND DATA PROCESSING
# ============================================================

print()
print("========================================")
print("5. OPTIMIZE LOOPS AND DATA PROCESSING")
print("========================================")

# Normal for loop

numbers = []

for i in range(10):
    numbers.append(i * 2)

print("Using normal loop:", numbers)


# Optimized approach - List comprehension

optimized_numbers = [i * 2 for i in range(10)]

print("Using list comprehension:", optimized_numbers)
# ============================================================
# 6. COMPARE LIST VS GENERATOR APPROACHES
# ============================================================

print()
print("========================================")
print("6. COMPARE LIST VS GENERATOR APPROACHES")
print("========================================")

import sys

# List

my_list = [x for x in range(100000)]

# Generator

my_generator = (x for x in range(100000))

print("List memory:", sys.getsizeof(my_list), "bytes")
print("Generator memory:", sys.getsizeof(my_generator), "bytes")

# ============================================================
# 7. UNDERSTAND MULTIPROCESSING
# ============================================================

print()
print("========================================")
print("7. UNDERSTAND MULTIPROCESSING")
print("========================================")

import multiprocessing


def worker(number):
    print("Process is working on:", number)


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
    # ============================================================
# 7. UNDERSTAND MULTIPROCESSING
# ============================================================

print()
print("========================================")
print("7. UNDERSTAND MULTIPROCESSING")
print("========================================")

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

    print("Process 1 exit code:", process1.exitcode)
    print("Process 2 exit code:", process2.exitcode)

    print("All processes completed")
    # ============================================================
# 8. UNDERSTAND MULTITHREADING
# ============================================================

print()
print("========================================")
print("8. UNDERSTAND MULTITHREADING")
print("========================================")

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
# ============================================================
# 9. UNDERSTAND THE PYTHON GIL
# ============================================================

print()
print("========================================")
print("9. UNDERSTAND THE PYTHON GIL")
print("========================================")

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
# ============================================================
# 10. IMPLEMENT A MULTITHREADING EXAMPLE
# ============================================================

print()
print("========================================")
print("10. IMPLEMENT A MULTITHREADING EXAMPLE")
print("========================================")

import threading
import time


def download_file(file_name):
    print("Starting:", file_name)

    # Simulating file download / network waiting
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
# ============================================================
# 11. IMPLEMENT MULTIPROCESSING FOR CPU-INTENSIVE WORK
# ============================================================

print()
print("========================================")
print("11. MULTIPROCESSING FOR CPU-INTENSIVE WORK")
print("========================================")

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
    # ============================================================
# 12. ASYNCHRONOUS PROGRAMMING USING ASYNCIO
# ============================================================

print()
print("========================================")
print("12. ASYNCHRONOUS PROGRAMMING USING ASYNCIO")
print("========================================")

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
# ============================================================
# 13. CREATE ASYNCHRONOUS TASKS
# ============================================================

print()
print("========================================")
print("13. CREATE ASYNCHRONOUS TASKS")
print("========================================")

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
# ============================================================
# 14. COMPARE SYNCHRONOUS VS ASYNCHRONOUS EXECUTION
# ============================================================

print()
print("========================================")
print("14. SYNCHRONOUS VS ASYNCHRONOUS")
print("========================================")

import asyncio
import time


# ------------------------------------------------------------
# Synchronous Function
# ------------------------------------------------------------

def synchronous_task(name):
    print(name, "started")

    time.sleep(2)

    print(name, "finished")


# ------------------------------------------------------------
# Asynchronous Function
# ------------------------------------------------------------

async def asynchronous_task(name):
    print(name, "started")

    await asyncio.sleep(2)

    print(name, "finished")


# ------------------------------------------------------------
# Synchronous Execution
# ------------------------------------------------------------

print()
print("----- SYNCHRONOUS EXECUTION -----")

start_time = time.time()

synchronous_task("Sync Task 1")
synchronous_task("Sync Task 2")
synchronous_task("Sync Task 3")

end_time = time.time()

sync_time = end_time - start_time

print("Synchronous time:", sync_time, "seconds")


# ------------------------------------------------------------
# Asynchronous Execution
# ------------------------------------------------------------

print()
print("----- ASYNCHRONOUS EXECUTION -----")


async def run_async_tasks():

    start_time = time.time()

    await asyncio.gather(
        asynchronous_task("Async Task 1"),
        asynchronous_task("Async Task 2"),
        asynchronous_task("Async Task 3")
    )

    end_time = time.time()

    async_time = end_time - start_time

    print("Asynchronous time:", async_time, "seconds")


asyncio.run(run_async_tasks())
# ============================================================
# 15. BENCHMARK THE IMPLEMENTATIONS
# ============================================================

print()
print("========================================")
print("15. BENCHMARK THE IMPLEMENTATIONS")
print("========================================")

import time
import threading
import asyncio


# ------------------------------------------------------------
# Synchronous Implementation
# ------------------------------------------------------------

def sync_work():
    time.sleep(2)
    time.sleep(2)
    time.sleep(2)


# ------------------------------------------------------------
# Multithreading Implementation
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# Async Implementation
# ------------------------------------------------------------

async def async_work():
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    await asyncio.sleep(2)


async def run_async():
    await asyncio.gather(
        asyncio.sleep(2),
        asyncio.sleep(2),
        asyncio.sleep(2)
    )


# ------------------------------------------------------------
# Benchmark Synchronous
# ------------------------------------------------------------

start = time.time()

sync_work()

sync_time = time.time() - start


# ------------------------------------------------------------
# Benchmark Multithreading
# ------------------------------------------------------------

start = time.time()

run_threads()

thread_time = time.time() - start


# ------------------------------------------------------------
# Benchmark Async
# ------------------------------------------------------------

start = time.time()

asyncio.run(run_async())

async_time = time.time() - start


# ------------------------------------------------------------
# Display Results
# ------------------------------------------------------------

print("Synchronous time:", sync_time, "seconds")
print("Multithreading time:", thread_time, "seconds")
print("Async time:", async_time, "seconds")
# ============================================================
# 16. DOCUMENT PERFORMANCE DIFFERENCES
# ============================================================

print()
print("========================================")
print("16. PERFORMANCE COMPARISON REPORT")
print("========================================")

print()
print("PERFORMANCE RESULTS")
print("------------------------------")

print("Synchronous       : 6.001 seconds")
print("Multithreading    : 2.002 seconds")
print("Asynchronous      : 2.005 seconds")

print()
print("PERFORMANCE ANALYSIS")
print("------------------------------")

print("1. Synchronous execution runs tasks one by one.")
print("2. Multithreading is useful for I/O-bound tasks.")
print("3. Async programming is useful for I/O-bound waiting tasks.")
print("4. Multiprocessing is useful for CPU-intensive tasks.")
print("5. Python GIL limits CPU-bound threading in CPython.")
print("6. Generators can save memory compared with lists.")
print("7. timeit can be used to measure execution time.")

print()
print("CONCLUSION")
print("------------------------------")

print("For this I/O-bound example:")
print("Multithreading and Async were faster than Synchronous execution.")

print()
print("PY-ADV-04 TASKS COMPLETED")
print("------------------------------")
print("All 16 tasks completed successfully.")