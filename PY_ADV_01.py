# ==========================
# TASK 1 - *args
# ==========================

def numbers(*args):
    for value in args:
        print(value)


numbers(10, 20, 30, 40)
# ==========================
# TASK 2 - *args SUM
# ==========================

def add(*args):
    total = 0

    for number in args:
        total = total + number

    print(total)


add(10, 20, 30)
# ==========================
# TASK 3 - *args MULTIPLICATION
# ==========================

def multiply(*args):
    result = 1

    for number in args:
        result = result * number

    print(result)


multiply(2, 3, 4)

# ==========================
# TASK 4 - *args + len()
# ==========================

def show(*args):
    print("Number of values:", len(args))
    print("Values:", args)


show(10, 20, 30, 40)

# ==========================
# TASK 5 - **kwargs
# ==========================

def student(**kwargs):
    print(kwargs)


student(name="Anusha", age=20, city="Hyderabad")

# ==========================
# TASK 6 - **kwargs LOOP
# ==========================

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


student_details(name="Anusha", age=20, city="Hyderabad")

# ==========================
# TASK 7 - *args + **kwargs
# ==========================

def student_info(*args, **kwargs):
    print("Subjects:")

    for subject in args:
        print(subject)

    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)


student_info("Python", "Java", "SQL", name="Anusha", age=20)
# ==========================
# TASK 8 - Student Data
# ==========================

def student_data(*args, **kwargs):
    print("Subjects:")

    for subject in args:
        print(subject)

    print()
    print("Student Information:")

    for key, value in kwargs.items():
        print(key, ":", value)


student_data(
    "Python",
    "Java",
    "SQL",
    name="Anusha",
    age=20,
    city="Hyderabad"
)
# ==========================
# TASK 9 - Normal Function
# ==========================

def greet():
    print("Hello Anusha")


greet()
# ==========================
# TASK 10 - Function as Argument
# ==========================

def greet_user():
    print("Hello Anusha")


def call_function(func):
    func()


call_function(greet_user)
# ==========================
# TASK 11 - First Decorator
# ==========================

def my_decorator(func):

    def wrapper():
        print("Function started")

        func()

        print("Function finished")

    return wrapper


def greet_decorated():
    print("Hello Anusha")


greet_decorated = my_decorator(greet_decorated)

greet_decorated()
# ==========================
# TASK 12 - @ Decorator Syntax
# ==========================

def my_decorator_2(func):

    def wrapper():
        print("Function started")

        func()

        print("Function finished")

    return wrapper


@my_decorator_2
def welcome():
    print("Welcome to Python")


welcome()
# ==========================
# TASK 13 - Decorator with Arguments
# ==========================

def my_decorator_3(func):

    def wrapper(*args, **kwargs):
        print("Function started")

        func(*args, **kwargs)

        print("Function finished")

    return wrapper


@my_decorator_3
def add(a, b):
    print("Sum:", a + b)


add(10, 20)
# ==========================
# TASK 14 - Decorator + return
# ==========================

def my_decorator_4(func):

    def wrapper(*args, **kwargs):
        print("Function started")

        result = func(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper


@my_decorator_4
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Result:", result)
# ==========================
# TASK 15 - Practical Decorator
# ==========================

def login_check(func):

    def wrapper():
        print("Checking login...")

        func()

        print("Done")

    return wrapper


@login_check
def dashboard():
    print("Welcome to Dashboard")


dashboard()
# ==========================
# TASK 16 - Closure Basic
# ==========================

def outer():
    message = "Hello Anusha"

    def inner():
        print(message)

    inner()


outer()
# ==========================
# TASK 17 - Closure Return
# ==========================

def outer_function():
    message = "Hello from outer function"

    def inner_function():
        print(message)

    return inner_function


my_function = outer_function()

my_function()
# ==========================
# TASK 18 - Closure with Parameter
# ==========================

def multiplier(x):

    def multiply(number):
        return x * number

    return multiply


double = multiplier(2)

print("Double:", double(10))


triple = multiplier(3)

print("Triple:", triple(10))

# ==========================
# TASK 19 - Iterator Basic
# ==========================

numbers = [10, 20, 30]

my_iterator = iter(numbers)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# ==========================
# TASK 20 - next() Practice
# ==========================

colors = ["Red", "Green", "Blue"]

color_iterator = iter(colors)

first = next(color_iterator)
print("First:", first)

second = next(color_iterator)
print("Second:", second)

third = next(color_iterator)
print("Third:", third)

# ==========================
# TASK 21 - StopIteration
# ==========================

numbers = [10, 20, 30]

number_iterator = iter(numbers)

print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))


# ==========================
# TASK 22 - Handle StopIteration
# ==========================

numbers = [10, 20, 30]

number_iterator = iter(numbers)

try:
    print(next(number_iterator))
    print(next(number_iterator))
    print(next(number_iterator))
    print(next(number_iterator))
except StopIteration:
    print("No more values")

    # ==========================
# TASK 23 - for Loop with Iterator
# ==========================

numbers = [100, 200, 300, 400]

number_iterator = iter(numbers)

for number in number_iterator:
    print(number)

    # ==========================
# TASK 24 - Custom Iterator
# ==========================

class Counter:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number

        raise StopIteration


count = Counter(3)

print(next(count))
print(next(count))
print(next(count))

# ==========================
# TASK 25 - Custom Iterator with for Loop
# ==========================

class NumberCounter:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number

        raise StopIteration


counter = NumberCounter(5)

for number in counter:
    print(number)

    # ==========================
# TASK 26 - Generator Basic
# ==========================

def my_generator():

    yield 10
    yield 20
    yield 30


numbers = my_generator()

print(next(numbers))
print(next(numbers))
print(next(numbers))

# ==========================
# TASK 27 - Generator with for Loop
# ==========================

def numbers_generator():

    yield 100
    yield 200
    yield 300
    yield 400


for number in numbers_generator():
    print(number)

    # ==========================
# TASK 28 - Generator with Dynamic Values
# ==========================

def square_generator(numbers):

    for number in numbers:
        yield number * number


numbers = [1, 2, 3, 4, 5]

for result in square_generator(numbers):
    print(result)

    # ==========================
# TASK 29 - Lazy Evaluation
# ==========================

def lazy_numbers():

    print("Generating 1")
    yield 1

    print("Generating 2")
    yield 2

    print("Generating 3")
    yield 3


numbers = lazy_numbers()

print("Generator created")

print(next(numbers))
print(next(numbers))
print(next(numbers))

# ==========================
# TASK 30 - Generator Expression
# ==========================

numbers = (number * number for number in range(1, 6))

for number in numbers:
    print(number)

    # ==========================
# TASK 31 - List Comprehension
# ==========================

numbers = [number * number for number in range(1, 6)]

print(numbers)

# ==========================
# TASK 32 - List Comprehension with if
# ==========================

even_numbers = [number for number in range(1, 11) if number % 2 == 0]

print(even_numbers)

# ==========================
# TASK 33 - Dictionary Comprehension
# ==========================

squares = {number: number * number for number in range(1, 6)}

print(squares)

# ==========================
# TASK 34 - Set Comprehension
# ==========================

even_set = {number for number in range(1, 11) if number % 2 == 0}

print(even_set)

# ==========================
# TASK 35 - Comprehension with if-else
# ==========================

result = ["Even" if number % 2 == 0 else "Odd" for number in range(1, 6)]

print(result)
# ==========================
# TASK 1 - Custom Iterator
# ==========================

class NumberIterator:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number

        raise StopIteration


numbers = NumberIterator(5)

for number in numbers:
    print(number)
    # ==========================
# TASK 2 - Comprehensions
# ==========================

# List Comprehension
squares = [number * number for number in range(1, 6)]
print("Squares:", squares)


# Dictionary Comprehension
square_dict = {number: number * number for number in range(1, 6)}
print("Dictionary:", square_dict)


# Set Comprehension
even_numbers = {number for number in range(1, 11) if number % 2 == 0}
print("Even numbers:", even_numbers)

# ==========================
# TASK 3 - Lambda Functions
# ==========================

square = lambda number: number * number

print("Square:", square(5))


add = lambda a, b: a + b

print("Sum:", add(10, 20))

# ==========================
# PROBLEM 1 - Find Largest Number
# ==========================

numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)
# ==========================
# PROBLEM 2 - Reverse a String
# ==========================

text = "Python"

reversed_text = text[::-1]

print("Reverse:", reversed_text)

# ==========================
# PROBLEM 3 - Check Palindrome
# ==========================

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

    # ==========================
# PROBLEM 4 - Count Vowels
# ==========================

text = "Python Programming"

vowels = "aeiou"

count = 0

for character in text.lower():
    if character in vowels:
        count += 1

print("Vowels:", count)

# ==========================
# PROBLEM 5 - Sum of Numbers
# ==========================

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print("Total:", total)

# ==========================
# PROBLEM 6 - Find Even Numbers
# ==========================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)

# ==========================
# PROBLEM 7 - Remove Duplicates
# ==========================

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print("Unique numbers:", unique_numbers)

# ==========================
# PROBLEM 8 - Factorial
# ==========================

number = 5

factorial = 1

for value in range(1, number + 1):
    factorial *= value

print("Factorial:", factorial)

# ==========================
# TASK 5 & 6 - Edge Cases and Invalid Inputs
# ==========================

def factorial(number):

    if number < 0:
        return "Invalid input"

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -5:", factorial(-5))

# ==========================
# TASK 7 - Refactoring
# ==========================

def calculate_factorial(number):
    if number < 0:
        return "Invalid input"

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


print("5! =", calculate_factorial(5))
print("0! =", calculate_factorial(0))
print("-5! =", calculate_factorial(-5))
# ==========================
# TASK 8 - Test Cases
# ==========================

def test_calculate_factorial():

    assert calculate_factorial(5) == 120
    assert calculate_factorial(0) == 1
    assert calculate_factorial(-5) == "Invalid input"

    print("All tests passed")


test_calculate_factorial()

# Advanced Python Fundamentals

## Objective

Evaluate advanced Python fundamentals and programming logic.

## Topics Covered

1. Custom Iterators
2. Comprehensions
3. Lambda Functions
4. Problem Solving
5. Edge Cases
6. Invalid Inputs
7. Code Refactoring
8. Test Cases

## Custom Iterator

Implemented a custom iterator using `__iter__()` and `__next__()`.

The iterator generates numbers from 1 to a given limit.

## Comprehensions

Practiced:

- List comprehension
- Dictionary comprehension
- Set comprehension

## Lambda Functions

Implemented simple lambda functions for:

- Square calculation
- Addition

## Problem-Solving Solutions

Solved 8 programming problems:

1. Find Largest Number
2. Reverse a String
3. Check Palindrome
4. Count Vowels
5. Find Sum of Numbers
6. Find Even Numbers
7. Remove Duplicates
8. Find Factorial

## Edge Cases

Handled edge cases such as:

- Factorial of 0
- Empty or special inputs where applicable

## Invalid Inputs

Handled invalid factorial input such as negative numbers.

Example:

```text
Factorial of -5: Invalid input