print("========================================")
print("1. CREATE A PYTHON APPLICATION USING OOP")
print("========================================")


class Student:

    def show_details(self):
        print("Student Name: Anusha")
        print("Course: Python")
        print("Status: Learning")


student = Student()

student.show_details()
print()
print("========================================")
print("2. IMPLEMENT CLASSES AND OBJECTS")
print("========================================")


class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student("Anusha", "Python")
student2 = Student("Rahul", "Java")

student1.display()
student2.display()
print()
print("========================================")
print("3. USE INHERITANCE")
print("========================================")


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()
print()
print("========================================")
print("4. IMPLEMENT ABSTRACTION")
print("========================================")


from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")


car = Car()

car.start()
print()
print("========================================")
print("5. IMPLEMENT ENCAPSULATION")
print("========================================")


class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student = Student(90)

print("Student Marks:", student.get_marks())
print()
print("========================================")
print("6. USE POLYMORPHISM")
print("========================================")


class Dog:

    def sound(self):
        print("Dog says: Woof")


class Cat:

    def sound(self):
        print("Cat says: Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
    print()
print("========================================")
print("7. CLASS METHODS AND STATIC METHODS")
print("========================================")


class Student:

    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_school(cls):
        print("School Name:", cls.school_name)

    @staticmethod
    def welcome_message():
        print("Welcome to Python OOP")


student = Student("Anusha")

print("Student Name:", student.name)

Student.show_school()

Student.welcome_message()
print()
print("========================================")
print("8. MAGIC / DUNDER METHODS")
print("========================================")


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}"

    def __len__(self):
        return len(self.name)


student = Student("Anusha", 22)

print(student)

print("Length of student name:", len(student))
print()
print("========================================")
print("9. IMPLEMENT CUSTOM EXCEPTIONS")
print("========================================")


class InvalidAgeError(Exception):
    pass


def check_age(age):

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("Eligible for registration")


try:

    check_age(15)

except InvalidAgeError as error:

    print("Custom Exception:", error)
    print()
print("========================================")
print("10. PROPER EXCEPTION-HANDLING FLOW")
print("========================================")


try:

    number1 = 10
    number2 = 0

    result = number1 / number2

except ZeroDivisionError:

    print("Error: Cannot divide by zero")

else:

    print("Result:", result)

finally:

    print("Exception handling completed")
    print()
print("========================================")
print("11. USE CONTEXT MANAGERS")
print("========================================")


with open("student.txt", "w") as file:

    file.write("Student Name: Anusha\n")
    file.write("Course: Python\n")

print("File created successfully")

with open("student.txt", "r") as file:

    content = file.read()

print("File Content:")
print(content)
print()
print("========================================")
print("12. CREATE A CUSTOM CONTEXT MANAGER")
print("========================================")


class MyContextManager:

    def __enter__(self):
        print("Context started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Context ended")


with MyContextManager():

    print("Inside the context")
    print()
print("========================================")
print("13. FACTORY DESIGN PATTERN")
print("========================================")


class Car:

    def drive(self):
        print("Car is driving")


class Bike:

    def drive(self):
        print("Bike is driving")


class VehicleFactory:

    @staticmethod
    def create_vehicle(vehicle_type):

        if vehicle_type == "car":
            return Car()

        elif vehicle_type == "bike":
            return Bike()

        else:
            raise ValueError("Unknown vehicle type")


car = VehicleFactory.create_vehicle("car")
bike = VehicleFactory.create_vehicle("bike")

car.drive()
bike.drive()
print()
print("========================================")
print("14. SINGLETON DESIGN PATTERN")
print("========================================")


class Database:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


database1 = Database()
database2 = Database()

print("Database object 1:", id(database1))
print("Database object 2:", id(database2))
print("Same object:", database1 is database2)
print()
print("========================================")
print("15. REFACTOR DUPLICATE CODE")
print("========================================")


def calculate_total(price, quantity):
    return price * quantity


product1_total = calculate_total(100, 2)
product2_total = calculate_total(200, 3)
product3_total = calculate_total(50, 4)

print("Product 1 Total:", product1_total)
print("Product 2 Total:", product2_total)
print("Product 3 Total:", product3_total)

grand_total = product1_total + product2_total + product3_total

print("Grand Total:", grand_total)
print()
print("========================================")
print("16. DESIGN DECISIONS AND ARCHITECTURE")
print("========================================")

print()
print("DESIGN DECISIONS")
print("------------------------------")

print("1. OOP was selected to organize the application using classes and objects.")
print("2. Inheritance was used to reuse functionality from a parent class.")
print("3. Abstraction was used to hide implementation details.")
print("4. Encapsulation was used to control access to data.")
print("5. Polymorphism was used to allow different behavior through the same method.")
print("6. Class methods were used to work with class-level data.")
print("7. Static methods were used for independent utility operations.")
print("8. Dunder methods were used to customize object behavior.")
print("9. Custom exceptions were created for application-specific errors.")
print("10. Exception handling was used to handle runtime errors safely.")
print("11. Context managers were used to manage resources automatically.")
print("12. Factory Pattern was used to centralize object creation.")
print("13. Singleton Pattern was used to ensure only one shared instance.")
print("14. Duplicate code was refactored into reusable functions.")

print()
print("ARCHITECTURE / FLOW")
print("------------------------------")

print("Application")
print("    |")
print("    +-- OOP Classes and Objects")
print("    |")
print("    +-- Inheritance")
print("    |")
print("    +-- Abstraction")
print("    |")
print("    +-- Encapsulation")
print("    |")
print("    +-- Polymorphism")
print("    |")
print("    +-- Exception Handling")
print("    |")
print("    +-- Context Managers")
print("    |")
print("    +-- Factory Pattern")
print("    |")
print("    +-- Singleton Pattern")
print("    |")
print("    +-- Refactored Reusable Code")

print()
print("PY-ADV-02 TASKS COMPLETED")
print("------------------------------")
print("All required OOP, exception handling, context manager,")
print("design pattern, and refactoring tasks were completed successfully.")