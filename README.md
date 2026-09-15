
<<<<<<< HEAD

````markdown
# Employee Management Backend

A Django backend project for Employee Management.

## Project Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
````

### 2. Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Django

```bash
python -m pip install django
```

### 4. Create Django Project

```bash
django-admin startproject employee_management .
```

### 5. Create Employees App

```bash
python manage.py startapp employees
```

### 6. Run Django Server

```bash
python manage.py runserver
```

Server URL:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Health Check API

### Endpoint

```text
GET /api/health/
```

### URL

```text
http://127.0.0.1:8000/api/health/
```

### Response

```json
{
    "status": "success",
    "message": "Employee Management Backend is running"
}
```

## Project Structure

```text
employee_management_backend/
│
├── employee_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── employees/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Main Files

### manage.py

Used to run Django commands.

Examples:

```bash
python manage.py runserver
python manage.py check
python manage.py startapp employees
```

### settings.py

Contains Django project configuration.

It includes:

* INSTALLED_APPS
* DATABASES
* MIDDLEWARE
* STATIC FILES
* Other project settings

### urls.py

Used for URL routing.

Project-level URL:

```text
/api/
```

Employee app URL:

```text
/api/health/
```

### models.py

Used to define database models.

Example:

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
```

### views.py

Contains request and response logic.

Health check view returns JSON response.

### admin.py

Used to configure Django Admin.

### apps.py

Contains application configuration for the employees app.

### employees/urls.py

Contains URL routes for the employees application.

## Testing

### Health Check Test

Open:

```text
http://127.0.0.1:8000/api/health/
```

Expected response:

```json
{
    "status": "success",
    "message": "Employee Management Backend is running"
}
```

### Invalid URL Test

Example:

```text
http://127.0.0.1:8000/api/invalid/
```

Expected result:

```text
404 Not Found
```

## Validation

Run Django system check:

```bash
python manage.py check
```

Expected output:

```text
System check identified no issues (0 silenced).
```

## Dependencies

Django dependencies are stored in:

```text
requirements.txt
```

Install dependencies using:

```bash
python -m pip install -r requirements.txt
```

## Current Status

* Django project created
* Virtual environment created
* Django installed
* Employees app created
* Employees app registered
* Project-level URL routing configured
* Employee app URL routing configured
* Health check API implemented
* Health check API tested successfully
* Invalid URL 404 testing completed
* requirements.txt created
* .gitignore create

8/9/26




```text
employee_management_backend
│
├── README.md
├── manage.py
├── employee_management/
└── employees/
```


# Y-ADV-02 — Django URLs, Views & Request/Response Flow

## Objective

Understand how a request travels through Django and implement employee-related views.

## Features Implemented

- Employee list view
- Employee detail view
- Application-level URL configuration
- Dynamic employee ID URL
- Meaningful URL names
- JsonResponse
- Sample employee data
- Invalid employee ID handling
- HTTP 404 status handling

## Project Structure

```text
employee_management_backend/
│
├── employee_management/
│   └── urls.py
│
├── employees/
│   ├── urls.py
│   └── views.py
│
├── manage.py
└── README.md
````

## URL Endpoints

### 1. Health Check

```text
GET /api/health/
```

### 2. Employee List

```text
GET /api/employees/
```

Returns all employees.

Example response:

```json
{
    "status": "success",
    "employees": [
        {
            "id": 1,
            "name": "Divya",
            "department": "Backend",
            "designation": "Python Developer"
        }
    ]
}
```

### 3. Employee Detail

```text
GET /api/employees/<id>/
```

Example:

```text
GET /api/employees/1/
```

Response:

```json
{
    "id": 1,
    "name": "Divya",
    "department": "Backend",
    "designation": "Python Developer"
}
```

## Invalid Employee ID

If an employee ID does not exist, the API returns HTTP 404.

Example:

```text
GET /api/employees/999/
```

Response:

```json
{
    "status": "error",
    "message": "Employee not found"
}
```

## Request/Response Flow

The Django request flow is:

```text
Client
   ↓
Project URL
   ↓
Application URL
   ↓
View
   ↓
JsonResponse
   ↓
Client
```

Example:

```text
GET /api/employees/1/
        ↓
employee_management/urls.py
        ↓
employees/urls.py
        ↓
employee_detail(request, id)
        ↓
JsonResponse
        ↓
Client
```

## Sample Employee Data

The application currently uses sample employee data:

| ID | Name   | Department | Designation      |
| -- | ------ | ---------- | ---------------- |
| 1  | Divya  | Backend    | Python Developer |
| 2  | Anusha | Frontend   | React Developer  |
| 3  | Rahul  | Testing    | QA Engineer      |

## Testing Completed

* Employee list endpoint tested
* Valid employee ID tested
* Invalid employee ID tested
* Invalid URL tested
* Empty employee list tested
* Django system check completed successfully

## Django System Check

Command:

```bash
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

## Git

### Branch

```text
feature/employee-views
```
09/09/26
## AY-03 — Django Models, Migrations & ORM
**Date:** 09-Sep-2026

### Completed Tasks

- Created `Employee` Django model
- Added employee fields:
  - employee_code
  - first_name
  - last_name
  - email
  - phone
  - department
  - designation
  - salary
  - joining_date
  - is_active
  - created_at
  - updated_at
- Added unique constraints for employee code and email
- Added default value for `is_active`
- Implemented `__str__()`
- Generated and applied Django migrations
- Created 15 employee records using Django ORM
- Retrieved all employees
- Filtered active employees
- Filtered inactive employees
- Filtered IT department employees
- Filtered employees with salary greater than 50,000
- Ordered employees by joining date
- Tested `get()`, `filter()`, and `exclude()`
- Tested ORM update operation
- Tested ORM delete operation
- Tested `DoesNotExist` error
- Tested and fixed incorrect ORM filter
- Tested and fixed incorrect migration
- Created Git branch `feature/employee-model`
- Completed Git commit

### Git Commit

`a11de51` — `feat: add employee model and orm operations`

10/09/26
## AY-04 — Django Admin & Employee CRUD

**Date:** 10-Sep-2026

### Objective

Complete the Employee CRUD application and configure the Django Admin interface.

### Django Admin

- Created Django superuser.
- Registered Employee model in Django Admin.
- Configured `list_display`.
- Configured `search_fields`.
- Configured `list_filter`.
- Configured `ordering`.
- Successfully logged into Django Admin.
- Added employees through Admin.
- Tested employee search.
- Tested employee filtering.

### Employee CRUD

Implemented:

- Create Employee
- Read Employee
- Update Employee
- Delete Employee

### Employee Form

Created `employees/forms.py` using Django `ModelForm`.

Implemented validation for:

- Employee code
- Email
- Salary
- Required fields

### Employee API Endpoints

```text
GET /api/employees/
POST /api/employees/

GET /api/employees/<id>/
PUT /api/employees/<id>/
PATCH /api/employees/<id>/
DELETE /api/employees/<id>/ 
### Testing Completed

- Valid employee creation
- Missing email
- Duplicate employee code
- Duplicate email
- Invalid salary
- Employee update
- Employee delete
- Invalid employee ID

### Debugging Exercises

- Duplicate email validation tested successfully.
- Missing form field validation tested successfully.
- Invalid redirect error (`NoReverseMatch`) introduced and fixed.
- Missing CSRF token issue tested and fixed for API testing using `@csrf_exempt`.

### Django System Check

```text
System check identified no issues (0 silenced).

### Git

**Branch:** `feature/employee-crud`

**Commit:** `dabe409 — feat: implement employee crud and admin`

Changes were successfully pushed to GitHub.

11/09/26

# Employee Management Backend

A Django-based Employee Management Backend application developed as part of the Django Fundamentals Week 1 tasks.

## Project Structure

```text
employee_management_backend/
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── employees/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
````

## Technologies Used

* Python
* Django
* SQLite
* Django ORM
* Django Admin
* JSON API

## Employee Model

The Employee model contains the following fields:

* employee_code
* first_name
* last_name
* email
* phone
* department
* designation
* salary
* joining_date
* is_active
* created_at
* updated_at

## API Endpoints

### Health Check

```text
GET /api/health/
```

Returns the application health status.

### List Employees

```text
GET /api/employees/
```

Returns all employees.

### Search / Filter Employees

```text
GET /api/employees/?department=IT
```

Returns employees belonging to the specified department.

### Create Employee

```text
POST /api/employees/
```

Creates a new employee.

Successful creation returns:
=======
# PY-ADV-08 — Employee REST API

## Project Overview

This project is a REST API developed using Flask.

The API provides CRUD operations for managing employee records.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Marshmallow
- Postman
- Pytest

## REST Architecture

REST stands for Representational State Transfer.

REST is an architectural style used to build web APIs.

The Employee REST API uses HTTP methods to communicate with the server.

## HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Completely update data |
| PATCH | Partially update data |
| DELETE | Delete data |

## Base URL

```text
http://127.0.0.1:5000
````

## Employee API Endpoints

| Method | Endpoint        | Description               |
| ------ | --------------- | ------------------------- |
| POST   | /employees      | Create employee           |
| GET    | /employees      | Get all employees         |
| GET    | /employees/{id} | Get employee by ID        |
| PUT    | /employees/{id} | Update employee           |
| PATCH  | /employees/{id} | Partially update employee |
| DELETE | /employees/{id} | Delete employee           |

## 1. Create Employee

### Request

```text
POST /employees
```

### JSON Body

```json
{
    "name": "Anusha",
    "email": "anusha@example.com",
    "department": "IT",
    "salary": 50000
}
```

### Success Response
>>>>>>> origin/main

```text
201 Created
```


### View Employee

```text
GET /api/employees/<id>/
```

Returns details of a specific employee.

### Update Employee

```text
PUT /api/employees/<id>/
```

Updates an employee.

### Partial Update Employee

```text
PATCH /api/employees/<id>/
```

Partially updates an employee.

### Delete Employee

```text
DELETE /api/employees/<id>/
```

Deletes an employee.

## HTTP Status Codes

* `200 OK` - Successful request
* `201 Created` - Employee successfully created
* `400 Bad Request` - Invalid input or duplicate data
* `404 Not Found` - Employee does not exist
* `405 Method Not Allowed` - Unsupported HTTP method

## Validation

The application validates:

* Required employee fields
* Unique employee code
* Unique email
* Salary cannot be negative
* Valid JSON request data

## Django Admin

Employee records can be managed through Django Admin.

Admin configuration includes:

* Employee list display
* Search functionality
* Department filtering
* Active status filtering
* Employee code ordering

## Logging

Basic application logging is implemented for:

* Health check requests
* Employee creation
* Employee updates
* Employee deletion

## Database and Migrations

Django migrations are used to create and update the Employee database table.

Migration commands:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Migration status can be checked using:

```powershell
python manage.py showmigrations
```

## Application Testing

The complete employee workflow was tested:

```text
Create Employee
      ↓
View Employee
      ↓
Update Employee
      ↓
Search Employee
      ↓
Filter Employee
      ↓
Delete Employee
```

All major CRUD operations were tested successfully.

## Debugging Challenge

The following controlled bugs were reproduced, identified, fixed, and tested:

### Bug 1 - Broken URL

An incorrect URL name caused a `NoReverseMatch` error.

Root cause was identified and the correct URL name was restored.

### Bug 2 - Incorrect ORM Query

An incorrect model field name caused a Django `FieldError`.

The query was corrected to use the actual `department` field.

### Bug 3 - Incorrect Response Status

The employee creation API returned `200 OK` instead of `201 Created`.

The response was corrected by adding:

```python
status=201
```

### Bug 4 - Missing Migration

A temporary model field was added without applying its migration.

The migration was created and applied successfully, and the temporary field was later removed with a cleanup migration.

## Final Verification

The Django project was verified using:

```powershell
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

The application server was also tested successfully.

## Week 1 Deliverable

Completed Django Fundamentals Week 1 deliverable including:

* Django Project
* Employees App
* Employee Model
* Database Migrations
* Django ORM
* Views
* URLs
* CRUD Operations
* Django Admin
* Form Validation
* HTTP Status Codes
* Error Handling
* Basic Logging
* API Testing
* Debugging
* Documentation
=======
Example:

```json
{
    "id": 1,
    "name": "Anusha",
    "email": "anusha@example.com",
    "department": "IT",
    "salary": 50000.0
}
```

## 2. Get All Employees

### Request

```text
GET /employees
```

### Success Response

```text
200 OK
```

## 3. Get Employee

### Request

```text
GET /employees/1
```

### Success Response

```text
200 OK
```

### Employee Not Found

```text
404 Not Found
```

Response:

```json
{
    "error": "Employee not found"
}
```

## 4. Update Employee

### Request

```text
PUT /employees/1
```

### JSON Body

```json
{
    "name": "Anusha Updated",
    "email": "anusha.updated@example.com",
    "department": "Python",
    "salary": 60000
}
```

### Success Response

```text
200 OK
```

## 5. Partial Update Employee

### Request

```text
PATCH /employees/1
```

### JSON Body

```json
{
    "salary": 70000
}
```

### Success Response

```text
200 OK
```

PATCH updates only the fields provided in the request.

## 6. Delete Employee

### Request

```text
DELETE /employees/1
```

### Success Response

```text
200 OK
```

Response:

```json
{
    "message": "Employee deleted successfully"
}
```

## Validation

The API validates employee input using Marshmallow.

Validation rules:

* Name must contain 2 to 100 characters.
* Email must be a valid email address.
* Department must contain 2 to 100 characters.
* Salary cannot be negative.

### Validation Error

```text
400 Bad Request
```

## Error Responses

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Request successful    |
| 201         | Employee created      |
| 400         | Validation error      |
| 404         | Employee not found    |
| 409         | Email already exists  |
| 500         | Database/server error |

## Database

The application uses SQLite as the database.

### Employee Table

| Column     | Type    | Description           |
| ---------- | ------- | --------------------- |
| id         | Integer | Primary key           |
| name       | String  | Employee name         |
| email      | String  | Unique employee email |
| department | String  | Employee department   |
| salary     | Float   | Employee salary       |

## Logging

The application uses Python logging.

Log file:

```text
employee_api.log
```

The application logs:

* Employee creation
* Employee update
* Employee deletion
* Database errors

## Postman Testing

The API was tested using Postman.

Tested operations:

* Create employee
* Get all employees
* Get employee by ID
* Update employee
* Partial update employee
* Delete employee
* Validation error
* Employee not found error

## How to Run

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run the application:

```powershell
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Project Status

The Employee REST API includes:

* Flask REST API
* REST architecture
* HTTP methods
* JSON requests
* JSON responses
* Request validation
* Exception handling
* Error responses
* SQLite database integration
* CRUD operations
* Logging
* Postman testing
* API documentation

15/09/26
# DRF-001 — Django REST Framework Setup & Serializers

## Objective

Set up Django REST Framework (DRF) in the Employee Management Backend and create read-only APIs using Django REST Framework serializers.

---

## 1. DRF Installation

Installed Django REST Framework using:

```powershell
pip install djangorestframework
````

DRF was successfully installed and added to the project requirements.

---

## 2. DRF Configuration

Added `rest_framework` to `INSTALLED_APPS` in:

```text
employee_management/settings.py
```

Configured basic DRF settings using:

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}
```

Verified the configuration using:

```powershell
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

---

## 3. API Structure

Created a separate API structure inside the `employees` application:

```text
employees/
└── api/
    ├── __init__.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

This keeps the REST API code separate from the existing Django application logic.

---

## 4. Employee Serializer

Created `EmployeeSerializer` using Django REST Framework `ModelSerializer`.

File:

```text
employees/api/serializers.py
```

The serializer exposes:

* id
* employee_code
* first_name
* last_name
* email
* phone
* department
* designation
* salary
* joining_date
* is_active
* created_at
* updated_at

The following fields are read-only:

* id
* created_at
* updated_at

---

## 5. Employee List API

Created the Employee List API:

```text
GET /api/v1/employees/
```

The API retrieves employee records using Django ORM:

```python
Employee.objects.all()
```

The queryset is serialized using:

```python
EmployeeSerializer(employees, many=True)
```

### Response

```text
HTTP 200 OK
Content-Type: application/json
```

The API successfully returns multiple employee records in JSON format.

---

## 6. Employee Detail API

Created the Employee Detail API:

```text
GET /api/v1/employees/<id>/
```

Example:

```text
GET /api/v1/employees/1/
```

The API retrieves a single employee using the employee ID.

### Existing Employee

For an existing employee ID:

```text
HTTP 200 OK
```

The employee details are returned as JSON.

### Non-existing Employee

For an employee ID that does not exist:

```text
GET /api/v1/employees/999/
```

Response:

```json
{
    "detail": "Employee not found."
}
```

Status:

```text
HTTP 404 Not Found
```

---

## 7. Invalid Employee ID Format

Tested an invalid ID:

```text
GET /api/v1/employees/abc/
```

Result:

```text
HTTP 404 Not Found
```

The URL uses:

```python
<int:id>
```

Therefore, non-integer values such as `abc` do not match the URL pattern.

---

## 8. API URL Configuration

API URLs are configured in:

```text
employees/api/urls.py
```

The project-level URL configuration includes the API using:

```python
path("api/v1/", include("employees.api.urls"))
```

Final API endpoints:

```text
GET /api/v1/employees/
GET /api/v1/employees/<id>/
```

---

## 9. Testing Completed

The following tests were completed:

* Employee list API
* Single employee API
* Multiple employee records
* Existing employee ID
* Non-existing employee ID
* Invalid employee ID format
* Empty database behavior

### Empty Database Behavior

When no employee records exist:

```python
Employee.objects.all()
```

returns an empty queryset, which is serialized with `many=True` as:

```json
[]
```

---

## 10. Debugging Completed

### Debugging 1 — Wrong Serializer Field

Intentionally added an invalid serializer field.

Result:

```text
ImproperlyConfigured
```

Root cause:

The field did not exist in the `Employee` model.

The invalid field was removed and the serializer was restored.

---

### Debugging 2 — Wrong Serializer Import

Temporarily imported:

```python
WrongSerializer
```

Result:

```text
ImportError
```

Root cause:

`WrongSerializer` did not exist.

Restored the correct import:

```python
from .serializers import EmployeeSerializer
```

---

### Debugging 3 — Incorrect URL Mapping

Temporarily changed:

```text
employees/
```

to:

```text
employee/
```

The API returned:

```text
HTTP 404 Not Found
```

Root cause:

The requested URL did not match the configured URL pattern.

The correct URL mapping was restored.

---

### Debugging 4 — Incorrect Queryset

Temporarily used:

```python
Employee.objects.filter(wrong_field="test")
```

Result:

```text
FieldError
```

Root cause:

`wrong_field` does not exist in the `Employee` model.

Restored the correct queryset:

```python
Employee.objects.all()
```

Retested successfully with:

```text
HTTP 200 OK
```

---

### Debugging 5 — Invalid Employee ID Handling

Tested:

```text
GET /api/v1/employees/999/
```

Result:

```text
HTTP 404 Not Found
```

Response:

```json
{
    "detail": "Employee not found."
}
```

The API correctly handles non-existing employee IDs.

---

## 11. Final API Summary

| Method | Endpoint                  | Purpose                | Status        |
| ------ | ------------------------- | ---------------------- | ------------- |
| GET    | `/api/v1/employees/`      | Retrieve all employees | 200 OK        |
| GET    | `/api/v1/employees/<id>/` | Retrieve one employee  | 200 OK        |
| GET    | `/api/v1/employees/999/`  | Non-existing employee  | 404 Not Found |
| GET    | `/api/v1/employees/abc/`  | Invalid ID format      | 404 Not Found |

---

## 12. Deliverables

* Django REST Framework installed
* DRF configured
* EmployeeSerializer created
* Employee List API created
* Employee Detail API created
* API URL configuration completed
* Invalid employee handling implemented
* API testing completed
* Debugging exercises completed
* README documentation updated




