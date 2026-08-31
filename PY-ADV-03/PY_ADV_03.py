print("========================================")
print("1. READ AND WRITE CSV FILES")
print("========================================")

import csv

# Write data to CSV file
with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Course", "Status"])
    writer.writerow(["Anusha", "Python", "Learning"])
    writer.writerow(["Rahul", "Java", "Completed"])
    writer.writerow(["Priya", "Python", "Learning"])

print("CSV file written successfully")


# Read data from CSV file
with open("students.csv", "r") as file:

    reader = csv.reader(file)

    print("CSV Data:")

    for row in reader:
        print(row)
        print()
print("========================================")
print("2. PROCESS JSON DATA")
print("========================================")

import json

student = {
    "name": "Anusha",
    "course": "Python",
    "status": "Learning"
}

# Convert Python dictionary to JSON
json_data = json.dumps(student, indent=4)

print("JSON Data:")
print(json_data)

# Write JSON to file
with open("data.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully")

# Read JSON from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Read JSON Data:")
print(loaded_data)
print()
print("========================================")
print("3. WORK WITH NESTED JSON")
print("========================================")

nested_data = {
    "student": {
        "name": "Anusha",
        "course": {
            "name": "Python",
            "level": "Advanced"
        },
        "skills": [
            "Python",
            "OOP",
            "JSON"
        ]
    }
}

print("Student Name:", nested_data["student"]["name"])
print("Course:", nested_data["student"]["course"]["name"])
print("Level:", nested_data["student"]["course"]["level"])
print("Skills:", nested_data["student"]["skills"])
print()
print("========================================")
print("4. CREATE DATA TRANSFORMATION FUNCTIONS")
print("========================================")


def transform_students(students):

    result = []

    for student in students:

        transformed = {
            "student_name": student["name"].upper(),
            "course": student["course"].upper()
        }

        result.append(transformed)

    return result


students = [
    {
        "name": "Anusha",
        "course": "Python"
    },
    {
        "name": "Rahul",
        "course": "Java"
    }
]

print("Original Data:")
print(students)

transformed_data = transform_students(students)

print("Transformed Data:")
print(transformed_data)
print()
print("========================================")
print("5. VALIDATE INCOMING DATA")
print("========================================")


def validate_student(student):

    if "name" not in student:
        return False

    if "course" not in student:
        return False

    if not student["name"]:
        return False

    if not student["course"]:
        return False

    return True


student = {
    "name": "Anusha",
    "course": "Python"
}


if validate_student(student):

    print("Student data is valid")

else:

    print("Student data is invalid")
    print()
print("========================================")
print("6. HANDLE MISSING AND INCORRECT VALUES")
print("========================================")


def clean_student(student):

    name = student.get("name", "Unknown")
    age = student.get("age", 0)

    if not isinstance(age, int):
        age = 0

    return {
        "name": name,
        "age": age
    }


student = {
    "name": "Anusha",
    "age": "twenty"
}

print("Original Data:", student)

cleaned_data = clean_student(student)

print("Cleaned Data:", cleaned_data)
print()
print("========================================")
print("7. WORK WITH PYTHON DATETIME")
print("========================================")

from datetime import datetime, timedelta

# Get current date and time
now = datetime.now()

print("Current Date and Time:", now)

# Get only date
print("Current Date:", now.date())

# Get only time
print("Current Time:", now.time())

# Format date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print("Formatted Date and Time:", formatted_date)

# Calculate tomorrow
tomorrow = now + timedelta(days=1)

print("Tomorrow:", tomorrow.date())
print()
print("========================================")
print("8. IMPLEMENT LOGGING")
print("========================================")

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")

print("Logging started successfully")

logging.info("Data processing started")

print("Data processing started")

logging.info("Data processing completed")

print("Data processing completed")
print()
print("========================================")
print("9. CONSUME A REST API USING PYTHON")
print("========================================")

import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/users"

try:

    with urllib.request.urlopen(url, timeout=10) as response:

        data = json.loads(response.read().decode())

    print("API request successful")
    print("Number of users:", len(data))

    print("First User:")
    print("Name:", data[0]["name"])
    print("Email:", data[0]["email"])

except Exception as error:

    print("API request failed:", error)
    print()
print("========================================")
print("10. HANDLE API ERRORS")
print("========================================")

import urllib.request
import urllib.error

url = "https://jsonplaceholder.typicode.com/invalid-url"

try:

    with urllib.request.urlopen(url, timeout=10) as response:
        print("API request successful")

except urllib.error.HTTPError as error:

    print("HTTP Error:", error.code)
    print("API resource was not found")

except urllib.error.URLError as error:

    print("URL Error:", error.reason)

except Exception as error:

    print("Unexpected Error:", error)

print("API error handling completed")
print()
print("========================================")
print("11. IMPLEMENT TIMEOUT HANDLING")
print("========================================")

import urllib.request
import urllib.error

url = "https://jsonplaceholder.typicode.com/users"

try:

    print("Sending API request...")

    with urllib.request.urlopen(url, timeout=5) as response:

        data = response.read()

    print("API request completed successfully")
    print("Response received")

except TimeoutError:

    print("API request timed out")

except urllib.error.URLError as error:

    print("Connection Error:", error.reason)

except Exception as error:

    print("Unexpected Error:", error)

print("Timeout handling completed")
print()
print("========================================")
print("12. PARSE API RESPONSES")
print("========================================")

import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/users"

try:

    with urllib.request.urlopen(url, timeout=10) as response:

        data = json.loads(response.read().decode())

    print("API response parsed successfully")

    print("User Details:")

    for user in data[:3]:

        name = user["name"]
        email = user["email"]
        city = user["address"]["city"]

        print("Name:", name)
        print("Email:", email)
        print("City:", city)
        print("------------------------------")

except Exception as error:

    print("Error parsing API response:", error)
    print()
print("========================================")
print("13. STORE PROCESSED RESULTS LOCALLY")
print("========================================")

import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/users"

try:

    with urllib.request.urlopen(url, timeout=10) as response:

        data = json.loads(response.read().decode())

    processed_users = []

    for user in data[:5]:

        processed_user = {
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        }

        processed_users.append(processed_user)

    with open("processed_users.json", "w") as file:

        json.dump(processed_users, file, indent=4)

    print("Processed results stored successfully")
    print("File: processed_users.json")
    print("Records stored:", len(processed_users))

except Exception as error:

    print("Error:", error)
    print()
print("========================================")
print("14. CREATE REUSABLE UTILITY MODULES")
print("========================================")

from utils import clean_name, is_valid_email, create_user_record


name = "  anusha  "
email = "anusha@example.com"
city = "Hyderabad"

print("Original Name:", name)

cleaned_name = clean_name(name)

print("Cleaned Name:", cleaned_name)

print("Valid Email:", is_valid_email(email))

user = create_user_record(
    name,
    email,
    city
)

print("User Record:", user)