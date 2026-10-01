
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

16/09/26

# DRF-002 — Generic Views & Complete CRUD API

**Date:** 17-Sep-2026

## Objective

Implemented complete Employee CRUD APIs using Django REST Framework Generic Views.

## Tasks Completed

### 1. Understand HTTP Methods

* GET — Read employee data
* POST — Create employee
* PUT — Full update
* PATCH — Partial update
* DELETE — Delete employee

### 2. List/Create API

Implemented `ListCreateAPIView` for:

* GET employee list
* POST new employee

Endpoint:

`/api/v1/employees/`

### 3. Employee Detail API

Implemented `RetrieveUpdateDestroyAPIView` for:

* GET employee by ID
* PUT full update
* PATCH partial update
* DELETE employee

Endpoint:

`/api/v1/employees/<id>/`

### 4. Employee CRUD Operations

Successfully implemented and tested:

* Create Employee
* Read Employee
* Update Employee
* Partial Update Employee
* Delete Employee

### 5. PostgreSQL Integration

Employee records were successfully created, updated, retrieved, and deleted using the PostgreSQL database.

### 6. API Validation

Implemented and tested:

* Required field validation
* Employee code validation
* Email validation
* Salary validation
* Duplicate employee code prevention
* Duplicate email prevention

### 7. API Testing

Tested the following responses:

* GET employee list — 200 OK
* POST valid employee — 201 Created
* GET employee by ID — 200 OK
* PUT employee — 200 OK
* PATCH employee — 200 OK
* DELETE employee — 204 No Content
* Invalid employee ID — 404 Not Found
* Missing required fields — 400 Bad Request
* Duplicate employee code — 400 Bad Request
* Duplicate email — 400 Bad Request

### 8. Debugging Exercises

Completed and fixed:

* Incorrect serializer validation
* Wrong HTTP status
* Incorrect lookup field
* Broken POST request
* DELETE not working

### 9. Generic Views Verification

Verified `ListCreateAPIView` for GET and POST operations.

Verified `RetrieveUpdateDestroyAPIView` for GET, PUT, PATCH, and DELETE operations.

### 10. Django System Check

Executed:

`python manage.py check`

Result:

**System check identified no issues (0 silenced).**

## Status

**DRF-002 — Generic Views & Complete CRUD API implementation, validation, testing, debugging, and PostgreSQL integration completed successfully.**

17/09/26

# DRF-003 — ViewSets, Routers & API Filtering

## Project Overview

This project implements an Employee REST API using Django REST Framework.

The API uses ViewSets and Routers to provide employee CRUD operations.

## Technologies Used

* Python
* Django
* Django REST Framework
* PostgreSQL
* Pytest

## Employee CRUD API

Base URL:

`http://127.0.0.1:8000/api/v1/`

### Employee List

**GET**

`/employees/`

Returns all employees.

### Create Employee

**POST**

`/employees/`

Creates a new employee.

### Retrieve Employee

**GET**

`/employees/{id}/`

Returns a specific employee.

### Update Employee

**PUT**

`/employees/{id}/`

Updates all employee details.

### Partial Update

**PATCH**

`/employees/{id}/`

Updates selected employee fields.

### Delete Employee

**DELETE**

`/employees/{id}/`

Deletes an employee.

## ViewSet

The Employee API uses `ModelViewSet`.

It provides these actions:

* list
* retrieve
* create
* update
* partial_update
* destroy

## Router

A `DefaultRouter` is used to register the EmployeeViewSet.

The router automatically creates the CRUD API URLs.

## Custom Active Endpoint

**GET**

`/employees/active/`

Returns only active employees.

## Filtering

### Department Filter

`/employees/?department=Backend`

Returns employees from the Backend department.

### Active Filter

`/employees/?is_active=true`

Returns active employees.

### Salary Filter

`/employees/?salary_min=60000`

Returns employees with salary greater than or equal to 60000.

## Search

Search employees using:

`/employees/?search=Divya`

Search fields:

* first_name
* last_name
* email
* employee_code
* department

## Ordering

### Salary Ascending

`/employees/?ordering=salary`

### Salary Descending

`/employees/?ordering=-salary`

### Joining Date

`/employees/?ordering=joining_date`

## Combined Filtering

Example:

`/employees/?department=Backend&is_active=true&ordering=-salary`

This filters Backend employees, selects active employees, and orders them by salary in descending order.

## Validation

Employee validation includes:

* Employee code
* Email
* Salary
* Required fields
* Duplicate employee codes
* Duplicate email addresses

## Testing

Automated API tests were created using Pytest.

Test command:

`pytest tests/test_drf_api.py`

Result:

`6 passed`

The API was also tested manually using PowerShell.

## Debugging

The following debugging scenarios were checked:

* Serializer validation
* HTTP status codes
* Lookup field
* POST request
* DELETE functionality
* Router configuration
* Custom API action
* Filter parameters
* Search fields
* Ordering fields

## API Status Codes

* **200 OK** — Successful GET, PUT, PATCH
* **201 Created** — Successful POST
* **204 No Content** — Successful DELETE
* **400 Bad Request** — Invalid request data
* **404 Not Found** — Employee does not exist

## Project Status

DRF-003 ViewSets, Routers, CRUD operations, filtering, searching, ordering, validation, testing, and debugging have been completed successfully.

18/09/26

# DRF-004 - Pagination, API Validation, Documentation & Code Review

**Date:** 18-Sep-2026

**Project:** Employee Management Backend

**Technology:** Django, Django REST Framework, PostgreSQL

---

## Project Overview

Employee Management REST API v2 is a Django REST Framework project for managing employee records.

The API provides CRUD operations along with validation, filtering, searching, ordering, pagination, standardized error handling, API documentation, testing, performance checking, and code review.

---

## Technologies Used

* Python
* Django
* Django REST Framework
* PostgreSQL
* Pytest
* PowerShell
* VS Code

---

## 1. Pagination

DRF pagination was implemented using `PageNumberPagination`.

### Page Size

```text
5 employees per page
```

### Example Requests

```text
GET /api/v1/employees/?page=1
```

```text
GET /api/v1/employees/?page=2
```

### Pagination Response

```json
{
    "count": 30,
    "next": "http://127.0.0.1:8000/api/v1/employees/?page=2",
    "previous": null,
    "results": []
}
```

The following pagination fields were tested successfully:

* `count`
* `next`
* `previous`
* `results`

---

## 2. Serializer Validation

Employee serializer validation was implemented and tested.

### Employee Code

* Required
* Unique
* Must start with `EMP`
* Must contain numbers after `EMP`

Example:

```text
EMP101
```

### Email

* Required
* Valid email format
* Unique

### Salary

* Cannot be negative
* Cannot exceed `10000000`

### Joining Date

* Must be a valid date
* Cannot be a future date

### Phone

* Must contain exactly 10 digits

---

## 3. Standard API Error Handling

API errors were standardized to provide understandable responses.

### Employee Not Found

**Status Code:** `404 Not Found`

```json
{
    "detail": "Employee not found."
}
```

### Validation Error

**Status Code:** `400 Bad Request`

Example:

```json
{
    "email": [
        "Email already exists."
    ]
}
```

---

## 4. API Documentation

Complete API documentation was created in:

```text
docs/API-DOCUMENTATION.md
```

The documentation covers:

* Base URL
* Authentication
* GET employees
* POST employee
* GET employee detail
* PUT employee
* PATCH employee
* DELETE employee
* Active employees
* Filtering
* Searching
* Ordering
* Pagination
* Validation rules
* Error responses
* HTTP status codes
* API testing

---

## 5. API Endpoints

Base URL:

```text
http://127.0.0.1:8000/api/v1/
```

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| GET    | `/employees/`        | List employees            |
| POST   | `/employees/`        | Create employee           |
| GET    | `/employees/{id}/`   | Retrieve employee         |
| PUT    | `/employees/{id}/`   | Update employee           |
| PATCH  | `/employees/{id}/`   | Partially update employee |
| DELETE | `/employees/{id}/`   | Delete employee           |
| GET    | `/employees/active/` | Get active employees      |

---

## 6. Filtering

### Department Filter

```text
GET /api/v1/employees/?department=Backend
```

### Active Status Filter

```text
GET /api/v1/employees/?is_active=true
```

### Minimum Salary Filter

```text
GET /api/v1/employees/?salary_min=60000
```

---

## 7. Search

Employee search is supported using the `search` query parameter.

Example:

```text
GET /api/v1/employees/?search=Divya
```

Search fields:

* First name
* Last name
* Email
* Employee code
* Department

---

## 8. Ordering

### Salary Ascending

```text
GET /api/v1/employees/?ordering=salary
```

### Salary Descending

```text
GET /api/v1/employees/?ordering=-salary
```

### Joining Date

```text
GET /api/v1/employees/?ordering=joining_date
```

---

## 9. Combined Filtering

Multiple query parameters can be used together.

Example:

```text
GET /api/v1/employees/?department=Backend&is_active=true&ordering=-salary
```

This filters Backend employees, selects active employees, and orders them by salary in descending order.

---

## 10. API Testing

Automated API tests were implemented using Pytest.

Test command:

```powershell
pytest tests\test_drf_api.py
```

Test result:

```text
15 passed
```

The tests cover:

* Employee list
* Active employees
* Department filtering
* Search
* Salary ordering
* Combined filtering
* Pagination
* Employee creation
* Employee retrieval
* Employee update
* Partial update
* Employee deletion
* Duplicate email validation
* Negative salary validation
* Invalid employee ID

---

## 11. Performance Check

API performance was checked using local development testing.

### Response Time

The Employee List API was measured using PowerShell.

Approximate response time:

```text
0.142 seconds
142 milliseconds
```

This is a local development measurement and not a production benchmark.

### Query Count

Database query count was checked for retrieving five employees.

Result:

```text
Query Count: 1
Employees Retrieved: 5
```

Serializer behavior was also checked.

Result:

```text
Query Count: 1
Serialized Records: 5
```

No additional query was generated by the serializer for these flat employee records.

---

## 12. Code Review

The following files were reviewed:

```text
employees/api/views.py
employees/api/serializers.py
employee_management/urls.py
employees/models.py
employee_management/settings.py
```

The review covered:

* Code duplication
* Naming
* Validation
* HTTP status codes
* Error handling
* Security configuration
* Query efficiency
* Serializer behavior
* API documentation

No major issues were identified during the review.

---

## 13. Controlled Debugging

Five controlled defects were tested and fixed.

### 1. Pagination Not Working

Pagination configuration was temporarily disabled and then restored.

Pagination was verified successfully after the fix.

### 2. Duplicate Email Accepted

Duplicate email validation was tested.

The API correctly returns:

```text
400 Bad Request
```

when an existing email is submitted.

### 3. Invalid Employee Returns 500

Invalid employee ID handling was tested.

The API correctly returns:

```text
404 Not Found
```

with:

```json
{
    "detail": "Employee not found."
}
```

### 4. Search Field Not Working

Employee search was tested using the `search` query parameter.

Search returned the expected employee records successfully.

### 5. Incorrect HTTP Status / Error Response

Employee deletion with an invalid ID was tested.

The API returns:

```text
404 Not Found
```

with:

```json
{
    "detail": "Employee not found."
}
```

---

## 14. HTTP Status Codes

| Status Code | Meaning     |
| ----------- | ----------- |
| 200         | OK          |
| 201         | Created     |
| 204         | No Content  |
| 400         | Bad Request |
| 404         | Not Found   |

---

## 15. API Request Flow

```text
Client
   ↓
URL Router
   ↓
ViewSet
   ↓
Serializer
   ↓
Django ORM
   ↓
PostgreSQL
   ↓
Serializer
   ↓
HTTP Response
```

---

## 16. Project Structure

```text
employee_management_backend/
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── employees/
│   ├── api/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── routers.py
│   │
│   ├── migrations/
│   ├── models.py
│   └── ...
│
├── tests/
│   └── test_drf_api.py
│
├── docs/
│   └── API-DOCUMENTATION.md
│
├── manage.py
├── pytest.ini
└── README.md
```

---

## 17. Django System Check

The Django project configuration was verified using:

```powershell
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

---

## 18. Final Project Status

The following DRF-004 tasks were completed successfully:

* Pagination
* Serializer validation
* Standard API error handling
* API documentation
* API test collection
* Performance checking
* Code review
* Controlled debugging

### Test Result

```text
15 passed
```

### Django System Check

```text
System check identified no issues (0 silenced).
```

## DRF-004 Status

```text
COMPLETED
```
21/09/26
# DB-001 — PostgreSQL Setup & Django Database Migration

**Date:** 21-Sep-2026

## Project Overview

This task integrates PostgreSQL with the Django Employee Management Backend.

The development database was migrated from SQLite to PostgreSQL, and Django ORM was used to communicate with the PostgreSQL database.

---

## Objective

* Understand PostgreSQL database concepts.
* Install and configure PostgreSQL.
* Create a PostgreSQL database and user.
* Connect Django with PostgreSQL.
* Configure database credentials using environment variables.
* Run Django migrations.
* Store and retrieve Employee records using Django ORM.
* Test PostgreSQL CRUD operations.
* Verify database and application restart behavior.
* Debug common PostgreSQL connection issues.

---

## Technologies Used

* Python 3.13.14
* Django 6.1.1
* Django REST Framework
* PostgreSQL 18
* psycopg
* python-dotenv
* Django ORM

---

## PostgreSQL Configuration

### Database

```text
Database Name: employee_management
Database User: employee_admin
Host: localhost
Port: 5432
```

Database credentials are stored using environment variables.

### Environment Variables

The `.env` file contains the local database configuration.

Example:

```env
DB_NAME=employee_management
DB_USER=employee_admin
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

The real `.env` file is excluded from Git.

---

## PostgreSQL Driver

The following packages were installed:

```text
psycopg==3.3.6
psycopg-binary==3.3.6
python-dotenv==1.2.3
```

They are also included in `requirements.txt`.

---

## Django Database Configuration

Django was configured to use PostgreSQL instead of SQLite.

The database configuration reads the following environment variables:

```text
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

---

## Migrations

Django migrations were successfully created and applied.

Commands used:

```powershell
python manage.py makemigrations
python manage.py migrate
```

All required migrations completed successfully.

---

## Employee Data

A minimum of 30 Employee records were created successfully in PostgreSQL.

The Employee data was verified using Django ORM.

Employee fields include:

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

---

## Django ORM Queries

### Get All Employees

```python
Employee.objects.all()
```

### Get Active Employees

```python
Employee.objects.filter(is_active=True)
```

### Get Backend Employees

```python
Employee.objects.filter(department="Backend")
```

### Get Employees Ordered by Highest Salary

```python
Employee.objects.order_by("-salary")
```

All four required ORM queries were executed successfully.

---

## CRUD Testing

PostgreSQL CRUD operations were tested using Django ORM.

### Create

A test employee was successfully created.

### Read

The created employee was successfully retrieved from PostgreSQL.

### Update

The employee salary was successfully updated from `45000` to `55000`.

### Delete

The test employee was successfully deleted.

All CRUD operations were completed successfully.

---

## PostgreSQL Restart Test

The PostgreSQL Windows service was restarted successfully.

Service:

```text
postgresql-x64-18
```

After restarting PostgreSQL, the Django application successfully reconnected to the database.

Employee count was verified as:

```text
Employee count: 30
```

---

## Django Restart Test

The Django development server was restarted successfully.

The following checks passed:

```text
System check identified no issues (0 silenced).

Starting WSGI development server at http://127.0.0.1:8000/
```

Django successfully connected to PostgreSQL after restart.

---

## Connection Verification

The PostgreSQL connection was verified using Django:

```python
from django.db import connection

connection.ensure_connection()
```

Result:

```text
PostgreSQL connection successful
```

---

## Debugging

The following PostgreSQL configuration items were verified.

### Database Name

```text
employee_management
```

### Database User

```text
employee_admin
```

### Database Password

The password was loaded successfully through the environment configuration.

### Database Host

```text
localhost
```

### Database Port

```text
5432
```

Common PostgreSQL connection issues considered:

1. Wrong database name
2. Wrong database password
3. Wrong database port
4. Missing PostgreSQL driver
5. Missing environment variable
6. PostgreSQL service not running

All required connection settings were verified successfully.

---

## Security

* The real database password is stored only in the local `.env` file.
* The `.env` file is included in `.gitignore`.
* The `.env.example` file contains placeholder values only.
* The real database password must never be committed to Git.

---

## Documentation

The following documentation files were created or updated:

```text
POSTGRESQL_NOTES.md
README.md
.env.example
```

`POSTGRESQL_NOTES.md` contains explanations of:

* Database
* Schema
* Table
* Row
* Column
* Primary Key
* Foreign Key
* Index
* Constraint
* Django ORM examples

---

## Project Status

DB-001 — PostgreSQL Setup & Django Database Migration has been completed successfully.

Completed:

* PostgreSQL installation
* Database and user creation
* PostgreSQL driver installation
* Django PostgreSQL configuration
* Environment variable configuration
* `.env` protection
* Django migrations
* 30 Employee records
* Django ORM queries
* CRUD testing
* PostgreSQL restart testing
* Django restart testing
* PostgreSQL connection verification
* Debugging
* PostgreSQL documentation
* Git commit
* GitHub push

---

## Git Information

### Branch

`feature/postgresql-integration`

### Commit

`745fd30`

### Commit Message

`feat: integrate postgresql with django`

### Git Status

Working tree was clean after the DB-001 commit.

The PostgreSQL integration changes were successfully committed and pushed to the GitHub repository.
22/09/26
# DB-002 — Django Relationships

## Objective

Implemented realistic database relationships in the Employee Management System using Django ORM.

The following relationships were implemented:

* ForeignKey
* OneToOneField
* ManyToManyField

---

## 1. Department Model

Created the `Department` model with the following fields:

* `id`
* `name`
* `code`
* `description`
* `is_active`
* `created_at`

Added unique constraints for:

* Department name
* Department code

Created and tested 5 departments:

* Backend
* Frontend
* HR
* Finance
* QA

---

## 2. Employee → Department

Implemented a **ForeignKey** relationship between `Employee` and `Department`.

### Relationship

```text
Department (1) ─────────── Employee (Many)
```

One department can have multiple employees.

The relationship uses:

```python
department = models.ForeignKey(
    Department,
    on_delete=models.PROTECT,
    related_name="employees"
)
```

Existing employee department data was successfully migrated to the Department table.

---

## 3. Employee → EmployeeProfile

Created the `EmployeeProfile` model with:

* `id`
* `employee`
* `date_of_birth`
* `address`
* `emergency_contact`
* `blood_group`
* `profile_image`
* `created_at`
* `updated_at`

Implemented a **OneToOneField** relationship.

### Relationship

```text
Employee (1) ─────────── EmployeeProfile (1)
```

Each employee has one profile.

The relationship uses:

```python
employee = models.OneToOneField(
    Employee,
    on_delete=models.CASCADE,
    related_name="profile"
)
```

Created 30 employee profiles.

Duplicate profile creation was tested and prevented successfully.

---

## 4. Project Model

Created the `Project` model with:

* `id`
* `name`
* `project_code`
* `description`
* `client_name`
* `start_date`
* `end_date`
* `status`

Created 8 projects for testing the employee-project relationship.

---

## 5. Employee ↔ Project

Implemented a **ManyToManyField** relationship between `Employee` and `Project`.

### Relationship

```text
Employee (Many) ─────────── Project (Many)
```

One employee can work on multiple projects.

One project can have multiple employees.

The relationship uses:

```python
projects = models.ManyToManyField(
    "Project",
    related_name="employees",
    blank=True
)
```

All 30 employees were assigned to one or more projects.

---

## 6. Database Migrations

Created and applied the required migrations:

```text
0006_department.py
0007_employee_department_fk.py
0008_remove_employee_department_fk_and_more.py
0009_employeeprofile.py
0010_project.py
0011_employee_projects.py
```

All migrations were successfully applied.

---

## 7. Test Data

The following test data was created:

| Data                         | Count |
| ---------------------------- | ----: |
| Departments                  |     5 |
| Employees                    |    30 |
| Employee Profiles            |    30 |
| Projects                     |     8 |
| Employee-Project Assignments |    61 |

---

## 8. Relationship Queries

The following queries were implemented and tested successfully:

### Get all employees in Backend department

Filtered employees using the Department relationship.

### Get employee profile

Accessed an employee profile using the OneToOne relationship.

### Get projects assigned to an employee

Retrieved projects using the ManyToMany relationship.

### Get employees working on a project

Used the reverse ManyToMany relationship to retrieve employees.

### Get Backend employees working on a specific project

Filtered employees using both Department and Project relationships.

---

## 9. Testing

The following scenarios were tested successfully:

* ForeignKey relationship
* OneToOne relationship
* ManyToMany relationship
* Invalid department handling
* Employee without profile check
* Duplicate profile prevention
* Project with multiple employees
* Department and Project filtering

### Django System Check

```text
System check identified no issues (0 silenced).
```

---

## 10. Git Information

### Branch

```text
feature/database-relationships
```

### Commit

```text
0b574ae
```

### Commit Message

```text
feat: implement advanced employee relationships
```

The DB-002 changes were successfully committed and pushed to GitHub.

### GitHub Repository

https://github.com/anushavangipurapu/Python-Advanced

### GitHub Branch

https://github.com/anushavangipurapu/Python-Advanced/tree/feature/database-relationships

---

## 11. Final Status

**DB-002 — Django Relationships completed successfully.**

Implemented and tested:

* Department → Employee using ForeignKey
* Employee → EmployeeProfile using OneToOneField
* Employee ↔ Project using ManyToManyField
* Database migrations
* Test data
* Relationship queries
* Relationship testing
* Django system checks
* Documentation
* Git commit and GitHub push

23/09/26
# DB-003 — Advanced Django ORM Queries & Reporting

## 1. Task Overview

**Task:** DB-003 — Advanced Django ORM Queries & Reporting

### Objective

Learn and implement advanced Django ORM queries without unnecessary raw SQL.

The task covers:

- Q Objects
- F Expressions
- Aggregations
- Annotations
- Complex ORM queries
- Reporting APIs
- Edge-case verification

---

## 2. Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- Django ORM
- PowerShell
- VS Code
- Git

---

## 3. Q Objects

Implemented complex filtering using Django `Q()` objects.

### Example

Employees belonging to either Backend or Data departments:

```python
from django.db.models import Q
from employees.models import Employee

employees = Employee.objects.filter(
    Q(department__code="BE") |
    Q(department__code="DATA")
)

employees.values_list(
    "employee_code",
    "first_name",
    "department__name"
)
````

### Result

Backend employees were successfully retrieved using the `OR` condition.

---

## 4. F Expressions

Implemented database-side salary updates using Django `F()` expressions.

### Example

Increased the salary of Backend employees by 10%:

```python
from django.db.models import F
from employees.models import Employee

Employee.objects.filter(
    department__code="BE"
).update(
    salary=F("salary") * 1.10
)
```

### Result

15 Backend employee salary records were updated successfully.

The updated salary values were verified using Django ORM.

---

## 5. Aggregation

Implemented Django ORM aggregation using:

* `Count`
* `Sum`
* `Avg`
* `Min`
* `Max`

### Salary Report

```python
from django.db.models import Count, Sum, Avg, Min, Max

salary_report = Employee.objects.aggregate(
    total_employees=Count("id"),
    average_salary=Avg("salary"),
    maximum_salary=Max("salary"),
    minimum_salary=Min("salary"),
    total_salary=Sum("salary")
)
```

### Result

```text
Total Employees: 30
Average Salary: 57566.666666666667
Maximum Salary: 74800.00
Minimum Salary: 41000.00
Total Salary: 1727000.00
```

---

## 6. Annotation

Implemented department-level statistics using `annotate()`.

### Query

```python
from django.db.models import Count, Avg, Max
from employees.models import Department

department_report = Department.objects.annotate(
    employee_count=Count("employees"),
    average_salary=Avg("employees__salary"),
    maximum_salary=Max("employees__salary")
).values(
    "name",
    "employee_count",
    "average_salary",
    "maximum_salary"
)
```

### Result

| Department | Employees | Average Salary | Maximum Salary |
| ---------- | --------- | -------------- | -------------- |
| HR         | 0         | None           | None           |
| QA         | 0         | None           | None           |
| Finance    | 0         | None           | None           |
| Frontend   | 15        | 55000          | 69000          |
| Backend    | 15        | 60133.33       | 74800          |

---

# 7. Complex ORM Queries

## A. Departments Having More Than 5 Employees

```python
Department.objects.annotate(
    employee_count=Count("employees")
).filter(
    employee_count__gt=5
).values(
    "name",
    "employee_count"
)
```

### Result

```text
Backend   - 15 employees
Frontend  - 15 employees
```

---

## B. Employees Earning More Than Their Department Average

Used `OuterRef`, `Subquery`, `Avg`, and `F`.

```python
from django.db.models import OuterRef, Subquery, Avg, F

department_average = Employee.objects.filter(
    department=OuterRef("department")
).values(
    "department"
).annotate(
    average_salary=Avg("salary")
).values(
    "average_salary"
)

high_earning_employees = Employee.objects.annotate(
    department_average=Subquery(department_average)
).filter(
    salary__gt=F("department_average")
).values(
    "employee_code",
    "first_name",
    "salary",
    "department__name",
    "department_average"
)
```

### Result

14 employees earning more than their respective department average were identified.

---

## C. Projects Having More Than 3 Employees

```python
from django.db.models import Count
from employees.models import Project

Project.objects.annotate(
    employee_count=Count("employees")
).filter(
    employee_count__gt=3
).values(
    "project_code",
    "name",
    "employee_count"
)
```

### Result

Projects with more than 3 employees were successfully identified.

---

## D. Employees Working on Multiple Projects

```python
Employee.objects.annotate(
    project_count=Count(
        "projects",
        distinct=True
    )
).filter(
    project_count__gt=1
).values(
    "employee_code",
    "first_name",
    "project_count"
)
```

### Result

Employees assigned to multiple projects were successfully identified.

---

## E. Employees Without an Assigned Project

```python
Employee.objects.filter(
    projects__isnull=True
).values(
    "employee_code",
    "first_name"
)
```

### Result

```text
[]
```

All current employees have at least one project assignment.

---

# 8. Reporting APIs

Implemented the following reporting APIs:

### Department Summary

```text
GET /api/v1/reports/department-summary/
```

### Project Summary

```text
GET /api/v1/reports/project-summary/
```

### Salary Summary

```text
GET /api/v1/reports/salary-summary/
```

---

# 9. Department Summary API

### Endpoint

```text
GET http://127.0.0.1:8000/api/v1/reports/department-summary/
```

### Response Structure

```json
{
    "department": "Backend",
    "employee_count": 15,
    "average_salary": 60133.33,
    "maximum_salary": 74800
}
```

The API returns department-wise employee count and salary statistics.

---

# 10. Project Summary API

### Endpoint

```text
GET http://127.0.0.1:8000/api/v1/reports/project-summary/
```

### Response Structure

```json
{
    "project": "Employee Management System",
    "project_code": "PROJ001",
    "employee_count": 8
}
```

The API returns project-wise employee counts.

---

# 11. Salary Summary API

### Endpoint

```text
GET http://127.0.0.1:8000/api/v1/reports/salary-summary/
```

### Response

```json
{
    "total_employees": 30,
    "average_salary": 57566.666666666667,
    "maximum_salary": 74800.00,
    "minimum_salary": 41000.00,
    "total_salary": 1727000.00
}
```

---

# 12. Edge Case Testing

The following cases were tested successfully.

## Empty Departments

Verified departments with no employees.

```text
HR       - 0 employees
QA       - 0 employees
Finance  - 0 employees
```

## Departments With Employees

```text
Backend   - 15 employees
Frontend  - 15 employees
```

## Departments With More Than 5 Employees

```text
Backend   - 15
Frontend  - 15
```

## Projects Without Employees

```python
list(
    Project.objects.annotate(
        employee_count=Count("employees")
    ).filter(
        employee_count=0
    ).values(
        "project_code",
        "name"
    )
)
```

### Result

```text
[]
```

## Employees Without Projects

```python
list(
    Employee.objects.filter(
        projects__isnull=True
    ).values(
        "employee_code",
        "first_name"
    )
)
```

### Result

```text
[]
```

---

# 13. API Testing Summary

The following APIs were tested successfully:

| API                | Method | Status |
| ------------------ | ------ | ------ |
| Department Summary | GET    | 200 OK |
| Project Summary    | GET    | 200 OK |
| Salary Summary     | GET    | 200 OK |

---

# 14. Django System Check

Executed:

```powershell
python manage.py check
```

### Result

```text
System check identified no issues (0 silenced).
```

---

# 15. Project Structure

```text
employee_management_backend/
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── employees/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── reports/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── README.md
```

---

# 16. Reporting URL Configuration

### reports/urls.py

```python
from django.urls import path
from .views import (
    department_summary,
    project_summary,
    salary_summary
)

urlpatterns = [
    path(
        "department-summary/",
        department_summary,
        name="department-summary"
    ),
    path(
        "project-summary/",
        project_summary,
        name="project-summary"
    ),
    path(
        "salary-summary/",
        salary_summary,
        name="salary-summary"
    ),
]
```

### Main URL Configuration

```python
path(
    "api/v1/reports/",
    include("reports.urls")
)
```

---

# 17. Files Added / Updated

### Added

```text
reports/
├── views.py
├── urls.py
```

### Updated

```text
employee_management/urls.py
employee_management/settings.py
README.md
```

---

# 18. Verification Summary

The following Django ORM concepts were implemented and tested:

* Q Objects
* F Expressions
* Count
* Sum
* Avg
* Min
* Max
* annotate()
* aggregate()
* OuterRef
* Subquery
* Complex relationship traversal
* Filtering
* Reporting APIs

---

# 19. Key Learning Outcomes

Through this task, I learned how to:

1. Build complex filters using `Q()`.
2. Perform database-side updates using `F()`.
3. Calculate statistics using aggregation functions.
4. Generate grouped statistics using `annotate()`.
5. Compare employee salaries with department averages.
6. Query departments based on employee counts.
7. Query projects based on employee counts.
8. Find employees assigned to multiple projects.
9. Find employees without project assignments.
10. Build reporting APIs using Django REST Framework.
11. Verify ORM results against database data.
12. Handle empty and populated relationship cases.

---

# 20. Final Task Status

## DB-003 — Advanced Django ORM Queries & Reporting

| Requirement            | Status    |
| ---------------------- | --------- |
| Q Objects              | Completed |
| F Expressions          | Completed |
| Aggregations           | Completed |
| Annotations            | Completed |
| Complex ORM Queries    | Completed |
| Department Summary API | Completed |
| Project Summary API    | Completed |
| Salary Summary API     | Completed |
| Edge Case Testing      | Completed |
| API Testing            | Completed |
| Django System Check    | Completed |
| Documentation          | Completed |

---

# 21. Final Outcome

The **DB-003 — Advanced Django ORM Queries & Reporting** task was successfully implemented and tested.

The project now supports advanced Django ORM querying, database-side updates, aggregation, annotation, complex relationship queries, and reporting APIs.

All required task requirements were completed successfully.

24/09/26

# DB-004 — Query Optimization, N+1 Problems & Database Indexing

## 1. Task Overview

**Task:** DB-004 — Query Optimization, N+1 Problems & Database Indexing

### Objective

Identify and fix inefficient database queries in Django applications and improve database performance using Django ORM optimization techniques and appropriate database indexes.

### Topics Covered

* N+1 Query Problem
* Query Count Measurement
* `select_related()`
* `prefetch_related()`
* Performance Comparison
* Database Index Evaluation
* PostgreSQL Query Plans
* API Query Optimization
* API Testing
* Performance Verification

---

## 2. Technologies Used

* Python
* Django
* Django REST Framework
* PostgreSQL
* Django ORM
* PowerShell
* VS Code
* Postman
* Git

---

## 3. N+1 Query Problem

The N+1 query problem was identified while accessing related Employee data.

The following relationships were analyzed:

* Employee → Department
* Employee → EmployeeProfile
* Employee → Projects

Without optimization, Django generated repeated database queries for related objects.

---

## 4. Query Count Measurement

Django database query logging was used to measure the number of database queries.

### Before Optimization

The Employee data was retrieved and related Department, Profile, and Project data was accessed.

The initial test generated:

```text
91 queries
```

This confirmed the N+1 query problem.

---

## 5. select_related() Optimization

`select_related()` was implemented for ForeignKey and OneToOne relationships.

The following relationships were optimized:

* Employee → Department
* Employee → EmployeeProfile

### Optimized Query

```python
employees = Employee.objects.select_related(
    "department",
    "profile"
)
```

### Result

```text
Before optimization: 31 queries
After optimization: 1 query
```

The repeated queries for Department and Profile were reduced successfully.

---

## 6. prefetch_related() Optimization

`prefetch_related()` was implemented for the Employee → Projects ManyToMany relationship.

### Optimized Query

```python
employees = Employee.objects.prefetch_related("projects")
```

### Result

```text
2 queries
```

The Employee and Project data were retrieved efficiently without executing a separate query for every employee.

---

## 7. Combined Query Optimization

The complete Employee query was optimized using both `select_related()` and `prefetch_related()`.

```python
employees = (
    Employee.objects
    .select_related("department", "profile")
    .prefetch_related("projects")
)
```

This efficiently loads:

* Employee
* Department
* Employee Profile
* Projects

---

## 8. Before and After Performance Comparison

### Before Optimization

```python
connection.queries_log.clear()

employees = Employee.objects.all()

for employee in employees:
    employee.department.name
    employee.profile
    list(employee.projects.all())

before_queries = len(connection.queries)

print("Before optimization:", before_queries)
```

### Result

```text
Before optimization: 91 queries
```

### After Optimization

```python
connection.queries_log.clear()

employees = (
    Employee.objects
    .select_related("department", "profile")
    .prefetch_related("projects")
)

for employee in employees:
    employee.department.name
    employee.profile
    list(employee.projects.all())

after_queries = len(connection.queries)

print("After optimization:", after_queries)
```

### Result

```text
After optimization: 2 queries
```

### Performance Comparison

| Metric           | Before | After |
| ---------------- | -----: | ----: |
| Database Queries |     91 |     2 |

The database query count was successfully reduced from **91 queries to 2 queries**.

---

## 9. Database Index Evaluation

The following commonly searched, filtered, or ordered fields were evaluated:

* `employee_code`
* `email`
* `department`
* `is_active`
* `joining_date`

Existing database indexes were checked before adding new indexes.

### Existing PostgreSQL Indexes

```text
employees_employee_pkey
employees_employee_employee_code_key
employees_employee_email_key
employees_employee_employee_code_fb9b0c8f_like
employees_employee_email_14fffd5e_like
employees_employee_department_fk_id_f66e261d
```

### Index Evaluation

| Field           | Evaluation                                      |
| --------------- | ----------------------------------------------- |
| `employee_code` | Already indexed through unique constraint       |
| `email`         | Already indexed through unique constraint       |
| `department`    | Already indexed through ForeignKey              |
| `is_active`     | Evaluated based on filtering usage              |
| `joining_date`  | Evaluated based on filtering and ordering usage |

Duplicate indexes were not added where suitable indexes already existed.

---

## 10. PostgreSQL Query Plan Analysis

PostgreSQL `EXPLAIN ANALYZE` was used to understand query execution.

### Query

```sql
EXPLAIN ANALYZE
SELECT *
FROM employees_employee
WHERE employee_code = 'EMP001';
```

### Query Plan

```text
Seq Scan on employees_employee
```

### Execution Details

```text
Rows: 1
Rows Removed by Filter: 29
Planning Time: 7.151 ms
Execution Time: 0.076 ms
```

### Explanation

PostgreSQL selected a Sequential Scan because the Employee table contains only 30 records.

For a small table, scanning the table can be cheaper than using an index.

The existing index is still valid and available for larger datasets or queries where PostgreSQL determines that an index scan is more efficient.

---

## 11. PostgreSQL Query Plan Terms

### Sequential Scan

PostgreSQL checks rows sequentially from the table.

### Index Scan

PostgreSQL uses an index to locate matching rows.

### Cost

The estimated cost of executing a query.

### Rows

The number of rows expected or processed.

### Execution Time

The actual time taken to execute the query.

---

## 12. Employee Details API Optimization

An Employee Details API was implemented and optimized.

### Endpoint

```text
GET /api/employees/details/
```

The API returns:

* Employee information
* Department information
* Employee Profile
* Project information

### Optimized Queryset

```python
employees = (
    Employee.objects
    .select_related("department", "profile")
    .prefetch_related("projects")
)
```

The optimized queryset avoids unnecessary repeated database queries.

---

## 13. API Testing

The optimized API was tested successfully.

### Request

```text
GET http://127.0.0.1:8000/api/employees/details/
```

### Result

```text
Status Code: 200 OK
```

The API returned the required employee, department, profile, and project information.

The functional response remained unchanged after optimization.

---

## 14. API Query Count Verification

The optimized endpoint was tested using Django query capture.

### Result

```text
API Query Count: 2
```

The Employee Details API successfully returned the required data using only **2 database queries**.

---

## 15. Django System Check

The project was verified using:

```powershell
python manage.py check
```

### Result

```text
System check identified no issues (0 silenced).
```

---

## 16. Testing Summary

| Test                           | Status    |
| ------------------------------ | --------- |
| N+1 Problem Identification     | Completed |
| Query Count Measurement        | Completed |
| `select_related()` Testing     | Completed |
| `prefetch_related()` Testing   | Completed |
| Before/After Query Comparison  | Completed |
| Database Index Evaluation      | Completed |
| PostgreSQL Query Plan Analysis | Completed |
| Employee Details API           | Completed |
| API Response Testing           | Completed |
| API Query Count Verification   | Completed |
| Django System Check            | Completed |

---

## 17. Deliverables

The following deliverables were completed:

```text
QUERY_OPTIMIZATION.md
DATABASE_INDEXES.md
Optimized Employee Details Queryset
Performance Comparison
Employee Details API
API Query Count Verification
PostgreSQL Query Plan Analysis
```

---

## 18. Final Performance Result

### Before Optimization

```text
91 database queries
```

### After Optimization

```text
2 database queries
```

### Performance Improvement

```text
91 → 2 queries
```

The N+1 query problem was successfully identified and fixed using Django ORM relationship optimization.

---

## 19. Key Learning Outcomes

Through this task, I learned how to:

1. Identify the N+1 query problem.
2. Measure Django database query counts.
3. Identify repeated database queries.
4. Use `select_related()` for ForeignKey relationships.
5. Use `select_related()` for OneToOne relationships.
6. Use `prefetch_related()` for ManyToMany relationships.
7. Compare database performance before and after optimization.
8. Evaluate database indexes.
9. Avoid unnecessary duplicate indexes.
10. Analyze PostgreSQL query plans.
11. Understand Sequential Scan and Index Scan.
12. Understand query cost and execution time.
13. Optimize Django API database queries.
14. Verify that API responses remain functionally identical after optimization.

---

## 20. Final Task Status

### DB-004 — Query Optimization, N+1 Problems & Database Indexing

| Requirement                       | Status      |
| --------------------------------- | ----------- |
| N+1 Problem Identified            | ✅ Completed |
| Query Count Measured              | ✅ Completed |
| `select_related()` Implemented    | ✅ Completed |
| `prefetch_related()` Implemented  | ✅ Completed |
| Before/After Performance Compared | ✅ Completed |
| Database Indexes Evaluated        | ✅ Completed |
| PostgreSQL Query Plan Analyzed    | ✅ Completed |
| Employee Details API Optimized    | ✅ Completed |
| API Response Tested               | ✅ Completed |
| Query Count Verified              | ✅ Completed |
| Documentation Completed           | ✅ Completed |

### Final Outcome

The **DB-004 — Query Optimization, N+1 Problems & Database Indexing** task was successfully completed and tested.

The N+1 query problem was identified and optimized using `select_related()` and `prefetch_related()`.

The database query count was reduced from **91 queries to 2 queries**, while maintaining the same functional API response.

28/09/26
# SEC-001 — User Authentication & Secure Password Management

## Objective

Implement proper user authentication and understand Django password security.

## Tasks Completed

### 1. Authentication vs Authorization

Documented the difference between Authentication and Authorization.

* **Authentication** verifies the identity of a user.
* **Authorization** determines what an authenticated user is allowed to access or perform.

Documentation created in:

`AUTHENTICATION_NOTES.md`

### 2. Django User System

Reviewed Django's built-in `User` model and its important fields:

* `username`
* `email`
* `password`
* `first_name`
* `last_name`
* `is_active`
* `is_staff`
* `is_superuser`

Verified that Django does not store passwords as plain text.

### 3. Registration API

Implemented:

```text
POST /api/v1/auth/register/
```

Registration fields:

```json
{
    "username": "final_auth_test",
    "email": "final_auth_test@example.com",
    "password": "StrongPass@123",
    "password_confirm": "StrongPass@123",
    "first_name": "Anusha",
    "last_name": "V"
}
```

A successful registration returns HTTP `201 Created`.

### 4. Registration Validation

Implemented validation for:

* Required username
* Unique username
* Required email
* Valid email format
* Unique email
* Required password
* Password strength
* Password confirmation

Tested weak password such as:

```text
123
```

Django password validation correctly rejects weak passwords.

### 5. Secure Password Storage

Used Django's:

```python
User.objects.create_user()
```

instead of storing passwords directly.

Verified the database password value starts with:

```text
pbkdf2_sha256$
```

This confirms that the password is stored as a hash instead of plain text.

### 6. Login API

Implemented:

```text
POST /api/v1/auth/login/
```

The login API authenticates the username and password using Django authentication.

Successful login returns HTTP `200 OK`.

Invalid username or password returns an authentication error.

### 7. Account Validation

Implemented inactive-account validation.

Users with:

```python
is_active = False
```

cannot authenticate successfully.

### 8. API Testing

The following test cases were completed:

| Test Case             | Status |
| --------------------- | ------ |
| Valid Registration    | Passed |
| Duplicate Username    | Passed |
| Duplicate Email       | Passed |
| Weak Password         | Passed |
| Password Confirmation | Passed |
| Wrong Password        | Passed |
| Wrong Username        | Passed |
| Inactive User         | Passed |
| Missing Fields        | Passed |
| Invalid Email         | Passed |

### 9. Debugging Exercises

The following issues were intentionally introduced and fixed:

#### Incorrect Password Storage

Incorrect:

```python
User.objects.create(
    username="test_user",
    password="PlainPassword123"
)
```

Correct:

```python
User.objects.create_user(
    username="test_user",
    password="PlainPassword123"
)
```

#### Duplicate Email

Temporarily removed duplicate-email validation, tested the issue, and restored the validation.

#### Inactive User Login

Tested inactive-user authentication and restored the secure authentication flow.

#### Missing Password Validation

Temporarily removed password validation, tested weak password acceptance, and restored:

```python
validators=[validate_password]
```

## API Endpoints

### Register

```text
POST /api/v1/auth/register/
```

### Login

```text
POST /api/v1/auth/login/
```

## Security Measures

* Passwords are never stored as plain text.
* Django password hashing is used.
* Weak passwords are rejected.
* Duplicate usernames are rejected.
* Duplicate emails are rejected.
* Password confirmation is validated.
* Invalid credentials are rejected.
* Inactive users cannot authenticate.

## Files Created/Updated

```text
accounts/
├── serializers.py
├── views.py
└── urls.py

AUTHENTICATION_NOTES.md
```

## Validation Check

Django system check completed successfully:

```text
System check identified no issues (0 silenced).
```

## Conclusion

The **SEC-001 — User Authentication & Secure Password Management** task was implemented and tested successfully. User registration, validation, secure password storage, login authentication, inactive-account validation, debugging exercises, and API testing were completed.

25/09/26
# DB-005 — Database Transactions, Employee Transfer & Epic Review

## Overview

Implemented an Employee Department Transfer workflow using Django, Django REST Framework, and PostgreSQL.

The task focused on database transactions, employee department transfers, transfer history, validation, rollback handling, advanced Django ORM queries, query optimization, database indexes, and PostgreSQL query analysis.

---

## 1. EmployeeTransfer Model

Created the `EmployeeTransfer` model with the following fields:

* `employee`
* `from_department`
* `to_department`
* `reason`
* `transferred_by`
* `transferred_at`
* `status`

Supported transfer statuses:

* PENDING
* APPROVED
* REJECTED
* COMPLETED

The model uses ForeignKey relationships with Employee and Department.

---

## 2. EmployeeTransferService

Created `EmployeeTransferService` to handle employee department transfers.

The service performs the following operations:

1. Finds the employee.
2. Verifies that the employee exists.
3. Verifies that the employee is active.
4. Finds the target department.
5. Verifies that the target department exists.
6. Verifies that the target department is active.
7. Checks that the target department is different from the current department.
8. Validates the transfer reason.
9. Creates the employee transfer history.
10. Updates the employee department.
11. Saves the transfer operation.

---

## 3. Database Transactions

Implemented Django's `transaction.atomic()` for the employee transfer operation.

The transaction ensures that the complete transfer operation is treated as one database transaction.

If an error occurs during the operation, the database changes are rolled back.

---

## 4. Transfer API

Implemented:

```text
POST /api/v1/employees/<id>/transfer/
```

Example request:

```json
{
    "to_department": 3,
    "reason": "Project requirement"
}
```

The API updates the employee department and creates a transfer history record.

---

## 5. Transfer History API

Implemented:

```text
GET /api/v1/employees/<id>/transfer-history/
```

The API returns the employee's previous department transfers including:

* Transfer ID
* From department
* To department
* Reason
* Status
* Transfer date
* Employee information

---

## 6. Successful Transfer Testing

The following transfer scenarios were tested successfully:

```text
Backend → HR
HR → Finance
Finance → Backend
```

The employee department was updated successfully and transfer history records were created.

---

## 7. Validation Testing

The following validation scenarios were tested:

### Invalid Employee

```text
Employee not found.
```

### Invalid Department

```text
Target department not found.
```

### Same Department

```text
Employee is already in this department.
```

### Inactive Employee

```text
Employee is inactive.
```

### Missing Reason

```text
Transfer reason is required.
```

All required validation scenarios were tested successfully.

---

## 8. Transaction Rollback Testing

A failure scenario was intentionally created inside `transaction.atomic()`.

The employee department was temporarily changed and an intentional exception was raised.

The database automatically rolled back the department change.

The final department was verified to be the original department.

Example result:

```text
Before: Backend
Inside transaction: Frontend
Error: Intentional rollback test
After rollback: Backend
```

This confirmed that transaction rollback is working correctly.

---

## 9. PostgreSQL Connection Review

Verified Django's database configuration.

```text
Database Engine: django.db.backends.postgresql
Database Name: employee_management
Connection: postgresql
```

The Django application is successfully connected to PostgreSQL.

---

## 10. Database Relationships Review

Verified the required Django relationships:

```text
Employee → Department
ForeignKey

EmployeeProfile → Employee
OneToOneField

Employee ↔ Project
ManyToManyField

EmployeeTransfer → Department
ForeignKey
```

All required relationships were verified successfully.

---

## 11. Advanced ORM Review

Verified Django ORM aggregation using:

```python
annotate()
Count()
```

Department-wise employee counts were successfully retrieved.

Example result:

```text
HR       → 0
QA       → 0
Finance  → 0
Frontend → 14
Backend  → 16
```

Total employee records verified: 30.

---

## 12. Q and F Expressions

Verified Django ORM `Q()` and `F()` expressions.

Example:

```python
Q(is_active=True) | Q(salary__gte=50000)
```

Result:

```text
Q query count: 28
```

An `F()` expression query was also executed successfully.

```text
F query count: 0
```

---

## 13. Query Optimization Review

Verified the use of:

```python
select_related()
prefetch_related()
```

Test results:

```text
select_related queries: 1
prefetch_related queries: 2
```

This confirms that related data can be fetched efficiently and helps prevent N+1 query problems.

---

## 14. Database Index Review

Verified the Employee model indexes:

```text
employee_code db_index: False
employee_code unique: True

email db_index: False
email unique: True

department db_index: True
```

`employee_code` and `email` use `unique=True`, which provides unique database indexes.

---

## 15. PostgreSQL Query Analysis

Used PostgreSQL `EXPLAIN ANALYZE` to inspect query execution.

Example query:

```sql
EXPLAIN ANALYZE
SELECT *
FROM employees_employee
WHERE employee_code = 'EMP001';
```

The query plan showed:

```text
Seq Scan on employees_employee
Rows Removed by Filter: 29
Planning Time: 6.858 ms
Execution Time: 0.160 ms
```

The sequential scan is reasonable for the current small dataset of 30 employees.

---

## 16. Technologies Used

* Python
* Django
* Django REST Framework
* PostgreSQL
* Django ORM
* Django Transactions
* PostgreSQL EXPLAIN ANALYZE

---

## 17. Testing Summary

The following areas were tested successfully:

* Employee department transfer
* Transfer history
* Invalid employee validation
* Invalid department validation
* Same department validation
* Inactive employee validation
* Missing reason validation
* Transaction rollback
* PostgreSQL connection
* Database relationships
* ORM aggregation
* Q expressions
* F expressions
* Query optimization
* Database indexes
* PostgreSQL query analysis

---

## Conclusion

The DB-005 Employee Transfer workflow was implemented using Django ORM and PostgreSQL transactions.

The transfer API, transfer history, validations, transaction rollback, database relationships, ORM queries, query optimization, indexes, and PostgreSQL query analysis were implemented and tested successfully.

29/09/26
# SEC-002 — JWT Authentication & Protected APIs

## Objective

Implemented JWT-based authentication for the Django REST Framework Employee Management API and protected the Employee APIs using JWT authentication.

## Tasks Completed

### 1. Understand JWT

Learned the basic JWT structure:

* Header
* Payload
* Signature
* Access Token
* Refresh Token
* Token Expiration
* Signature Validation

### 2. Install JWT Authentication Package

Installed Django REST Framework Simple JWT:

```bash
pip install djangorestframework-simplejwt
```

Configured JWT authentication in Django REST Framework.

### 3. Configure JWT Authentication

Updated `settings.py` with JWT authentication:

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],

    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],

    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",

    "PAGE_SIZE": 5,
}
```

Configured token expiration:

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

### 4. Create Token APIs

Implemented JWT token endpoints:

```text
POST /api/v1/auth/token/
```

Used for generating access and refresh tokens.

```text
POST /api/v1/auth/token/refresh/
```

Used for generating a new access token using the refresh token.

### 5. Protect Employee APIs

Configured the Employee API to require authentication:

```python
permission_classes = [IsAuthenticated]
```

The Employee APIs can only be accessed with a valid JWT access token.

### 6. Test Without Token

Tested the Employee API without authentication.

Result:

```text
401 Unauthorized
```

Response:

```json
{
    "detail": "Authentication credentials were not provided."
}
```

This confirmed that anonymous requests are rejected.

### 7. Test With Valid Access Token

Tested the Employee API using a valid JWT access token.

Result:

```text
200 OK
```

The API successfully returned the employee records.

The response contained:

```text
count: 30
```

### 8. Test Token Refresh

Tested the refresh token API successfully.

Request:

```text
POST /api/v1/auth/token/refresh/
```

A new access token was successfully generated using the refresh token.

### 9. Test Invalid Token

Tested the Employee API with an invalid token.

Result:

```text
401 Unauthorized
```

The invalid token was rejected successfully.

### 10. Test Modified Token

Tested the API by modifying a valid JWT token.

The modified token failed authentication and was rejected by the JWT authentication system.

## Authentication Testing Summary

| Test               | Result                     |
| ------------------ | -------------------------- |
| No Token           | 401 Unauthorized           |
| Valid Access Token | 200 OK                     |
| Invalid Token      | 401 Unauthorized           |
| Modified Token     | 401 Unauthorized           |
| Refresh Token      | New Access Token Generated |

## API Endpoints

### Generate JWT Token

```text
POST /api/v1/auth/token/
```

Example request:

```json
{
    "username": "auth_test_user",
    "password": "AuthTest@12345"
}
```

Response:

```json
{
    "access": "...",
    "refresh": "..."
}
```

### Refresh JWT Token

```text
POST /api/v1/auth/token/refresh/
```

Example request:

```json
{
    "refresh": "YOUR_REFRESH_TOKEN"
}
```

Response:

```json
{
    "access": "NEW_ACCESS_TOKEN"
}
```

### Protected Employee API

```text
GET /api/v1/employees/
```

Authorization:

```text
Bearer ACCESS_TOKEN
```

## Security

* JWT authentication is enabled for protected APIs.
* Access tokens are short-lived.
* Refresh tokens are used to obtain new access tokens.
* Requests without authentication are rejected.
* Invalid tokens are rejected.
* Modified tokens are rejected.
* Employee APIs require authenticated users.

## Result

JWT authentication was successfully configured and integrated with the Django REST Framework Employee Management API. Token generation, token refresh, protected API access, invalid token handling, and modified token validation were tested successfully.

30/09/26

# DAY 18 — 30-Sep-2026

# Jira Task: SEC-003 — Role-Based Access Control & Permissions

## Objective

Implement role-based authorization so that different users can perform different operations based on their assigned roles and ownership.

The four required roles are:

* ADMIN
* HR
* MANAGER
* EMPLOYEE

---

# Step 1 — Define Roles

The following roles were defined and their responsibilities were documented.

## ADMIN

* Can manage employee information.
* Can create employees.
* Can update employees.
* Can delete employees.
* Can access permitted employee information.

## HR

* Can manage employee information.
* Can create employees.
* Can update employees.
* Can view employees.
* Cannot perform restricted delete operations.

## MANAGER

* Can view employees within the permitted business scope.
* Cannot create employees.
* Cannot perform unrestricted update operations.
* Cannot delete employees.

## EMPLOYEE

* Can access their own permitted information.
* Cannot create employees.
* Cannot delete employees.
* Employee data access is restricted based on ownership.

---

# Step 2 — Add User Role

A role mechanism was added to associate a Django user with an employee profile.

The Employee model contains:

* User relationship
* Role field
* Role choices

Supported role values:

```text
ADMIN
HR
MANAGER
EMPLOYEE
```

The user-to-employee relationship is used to identify the authenticated user's role and ownership.

---

# Step 3 — Create Custom Permission Classes

A custom `permissions.py` file was created in the employees application.

The following permission classes were implemented:

```text
IsAdmin
IsHR
IsManager
IsEmployee
```

Each permission class checks:

1. Whether the user is authenticated.
2. Whether the user has an employee profile.
3. Whether the employee profile contains the required role.

Example permission structure:

```python
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "employee_profile")
            and request.user.employee_profile.role == "ADMIN"
        )
```

The same role-based permission approach was implemented for HR, Manager, and Employee roles.

---

# Step 4 — Protect Employee APIs

The Employee APIs were protected according to the documented permission matrix.

## Permission Matrix

| API Operation   | ADMIN | HR         | MANAGER    | EMPLOYEE |
| --------------- | ----- | ---------- | ---------- | -------- |
| List Employees  | Yes   | Yes        | Yes        | Own only |
| Create Employee | Yes   | Yes        | No         | No       |
| Update Employee | Yes   | Yes        | Restricted | Own only |
| Delete Employee | Yes   | Restricted | No         | No       |
| Own Profile     | Yes   | Yes        | Yes        | Yes      |

The permission rules were applied to the Employee ViewSet.

Different API actions use different permission combinations.

---

# Step 5 — Ownership-Based Authorization

The following endpoint was implemented:

```text
GET /api/v1/profile/me/
```

The endpoint retrieves the authenticated user's employee profile.

The ownership rule ensures that an employee cannot access another employee's profile through the protected employee API.

## Expected Behavior

```text
Employee A → Employee A profile
        ✅ Allowed

Employee A → Employee B profile
        ❌ Denied
```

The employee queryset is restricted to the authenticated employee's own profile.

---

# Step 6 — Permission Testing

The following test users were created for role-based authorization testing:

```text
admin_test
hr_test
manager_test
employee_test
```

Each user was assigned the corresponding role.

## Role Testing

### ADMIN

Tested:

* List employees
* Create employee
* Update employee
* Delete employee

### HR

Tested:

* List employees
* Create employee
* Update employee
* Delete employee restriction

### MANAGER

Tested:

* List employees
* Create employee restriction
* Update employee restriction
* Delete employee restriction

### EMPLOYEE

Tested:

* List permitted employee information
* Create employee restriction
* Update restriction
* Delete employee restriction
* Own employee information access

---

# Unauthorized User Testing

An unauthenticated request was tested against the protected Employee API.

Expected response:

```text
Authentication credentials were not provided.
```

The protected API correctly requires authentication.

---

# Cross-User Authorization Testing

An employee attempted to access another employee's information.

Example:

```text
Employee A → Employee B
```

The request was denied because the employee queryset is restricted to the authenticated user's own profile.

Expected result:

```text
Employee not found.
```

This prevents unauthorized cross-user data access.

---

# Debugging Exercises

The following authorization vulnerabilities were considered and tested:

## 1. Employee can delete employee

Expected:

```text
EMPLOYEE → DELETE
❌ Denied
```

The delete operation is restricted to the ADMIN role.

## 2. Manager can access admin operation

Expected:

```text
MANAGER → CREATE/ADMIN operation
❌ Denied
```

Manager permissions do not include unrestricted employee creation.

## 3. Employee can view another employee

Expected:

```text
EMPLOYEE A → EMPLOYEE B
❌ Denied
```

Ownership-based queryset filtering prevents cross-user access.

---

# Files and Deliverables

The following deliverables were implemented:

```text
employees/
│
├── permissions.py
│
├── api/
│   └── views.py
│
└── models.py
```

Additional documentation:

```text
ROLE_PERMISSIONS.md
README.md
```

The implementation includes:

* Role configuration
* Custom permission classes
* Permission matrix
* Protected RBAC APIs
* Ownership-based authorization
* Authorization test cases

---

# Authorization Flow

```text
User Login
    ↓
Authenticated User
    ↓
Employee Profile
    ↓
User Role
    ↓
Permission Class
    ↓
API Authorization
    ↓
Allow / Deny Request
```

---

# Security Validation

The following authorization scenarios were verified:

* Authenticated ADMIN access
* Authenticated HR access
* Authenticated MANAGER access
* Authenticated EMPLOYEE access
* Unauthorized user access
* Cross-user employee access
* Role-based create permissions
* Role-based update permissions
* Role-based delete permissions
* Ownership-based access restrictions

---

# Git

The RBAC implementation was developed using the following feature branch:

```powershell
git checkout -b feature/rbac-permissions
```

Changes can be staged using:

```powershell
git add .
```

Commit message:

```powershell
git commit -m "feat: implement role based access control"
```

---

# Acceptance Criteria

The SEC-003 task covers the following acceptance criteria:

* Four roles implemented.
* Permission classes implemented.
* API permissions enforced.
* Ownership rules implemented.
* Cross-user access prevented.
* All roles tested.
* Unauthorized access tested.
* Authorization vulnerabilities tested and fixed.
* Required documentation created.
* Git commit completed.

---

# Conclusion

The SEC-003 task implements role-based access control for the Employee Management API using Django REST Framework permissions.

The system differentiates access between ADMIN, HR, MANAGER, and EMPLOYEE users and applies role-based and ownership-based authorization to protected Employee APIs.

1/10/26

# AY 19 — 01-Oct-2026

# Jira Task: SEC-004 — Django & API Security Hardening

## Objective

Identify, review, test, and address common security weaknesses in the Django REST API.

The security hardening work covered security configuration, secret management, CORS, CSRF, input validation, SQL injection awareness, sensitive data exposure, rate limiting, authorization testing, and OWASP API Security concepts.

---

# Step 1 — Security Configuration Review

Reviewed the following Django security settings:

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- CORS configuration
- CSRF configuration
- `SESSION_COOKIE_SECURE`
- `CSRF_COOKIE_SECURE`
- `SECURE_SSL_REDIRECT`

Reviewed the difference between development and production security configurations.

Verified the project using:

```powershell
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

Security configuration review completed successfully.

---

# Step 2 — Secret Management

Reviewed sensitive configuration values including:

- `SECRET_KEY`
- Database credentials
- JWT-related secrets
- Email password
- API keys

Created and reviewed:

```text
.env.example
```

Example configuration:

```text
DB_NAME=employee_management
DB_USER=employee_admin
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=your_secret_key
JWT_SECRET=your_jwt_secret
EMAIL_PASSWORD=your_email_password
API_KEY=your_api_key
```

Verified that the actual `.env` file is ignored by Git.

Verified using:

```powershell
git check-ignore .env
```

Result:

```text
.env
```

Therefore, actual environment secrets are not tracked by Git.

---

# Step 3 — CORS Configuration

Reviewed the project's CORS configuration.

Configured a specific allowed origin:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

Verified that:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

is not enabled.

Reviewed why allowing all origins should not be blindly used in production.

Configuration validation:

```powershell
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

CORS configuration review completed.

---

# Step 4 — CSRF

Reviewed Django CSRF protection and its importance for browser-based cookie authentication.

Verified that Django CSRF middleware is enabled:

```text
django.middleware.csrf.CsrfViewMiddleware
```

Reviewed the project's JWT-based authentication approach.

Identified that some legacy function-based employee views use:

```python
@csrf_exempt
```

Created:

```text
CSRF_REVIEW.md
```

The document records the CSRF configuration, authentication approach, and security considerations.

CSRF review completed.

---

# Step 5 — Input Validation

Reviewed and tested API input validation.

The following cases were reviewed/tested:

- Empty values
- Invalid data types
- Unexpected fields
- Invalid IDs
- Invalid dates
- Negative salary values
- Malformed email values
- Required field validation
- Duplicate employee code
- Duplicate email
- Invalid JSON

Negative salary validation was confirmed.

Example validation response:

```json
{
    "status": "error",
    "message": "Salary cannot be negative"
}
```

Input validation review completed successfully.

---

# Step 6 — SQL Injection Awareness

Demonstrated safely how Django ORM queries are parameterized.

Tested a normal ORM query:

```python
Employee.objects.filter(first_name="Ravi")
```

Also tested an SQL-injection-style input as plain data:

```python
Employee.objects.filter(first_name="' OR '1'='1")
```

The ORM treated the value as data rather than executable SQL.

Reviewed an unsafe raw SQL pattern:

```python
query = f"SELECT * FROM employees_employee WHERE first_name = '{user_input}'"
```

Reviewed the safer parameterized approach:

```python
Employee.objects.raw(
    "SELECT * FROM employees_employee WHERE first_name = %s",
    ["Ravi"]
)
```

No real exploitable SQL injection vulnerability was introduced.

SQL injection awareness and safe ORM usage were completed.

---

# Step 7 — Sensitive Data Exposure

Reviewed API responses to ensure sensitive information such as the following is not exposed:

- Passwords
- Password hashes
- Private tokens
- Database credentials
- Internal secrets

Reviewed employee API responses and sensitive fields.

No password, password hash, JWT secret, database password, or API secret was found in the tested API responses.

Sensitive personal information such as employee contact and profile information was also reviewed for exposure and authorization requirements.

Sensitive data exposure review completed.

---

# Step 8 — Rate Limiting

Configured Django REST Framework throttling:

```python
"DEFAULT_THROTTLE_CLASSES": [
    "rest_framework.throttling.AnonRateThrottle",
    "rest_framework.throttling.UserRateThrottle",
],
```

Configured rates:

```python
"DEFAULT_THROTTLE_RATES": {
    "anon": "10/min",
    "user": "60/min",
},
```

Added anonymous throttling to sensitive authentication endpoints including:

- Registration
- Login

Password-related endpoint review was also performed; no separate password endpoint was implemented in the current application.

## Rate Limiting Test

Repeated login requests were sent using an invalid password.

The first 10 requests returned:

```text
400
```

After the configured limit was reached, subsequent requests returned:

```text
429
```

Example:

```text
Request 10 : 400
Request 11 : 429
Request 12 : 429
```

Response:

```json
{
    "detail": "Request was throttled. Expected available in 39 seconds."
}
```

### Result

Rate limiting configuration and actual throttling behavior were successfully verified.

---

# Step 9 — OWASP API Security Review

Reviewed the application against relevant OWASP API security concepts.

## 1. Broken Object Level Authorization (BOLA)

Tested access using an `EMPLOYEE` role.

The employee could access their own employee record:

```text
Employee ID: 42
```

When attempting to access another employee's record:

```text
Employee ID: 1
```

the API returned:

```json
{
    "detail": "Employee not found."
}
```

No unauthorized employee object data was exposed during the test.

### Result

BOLA test passed for the tested employee-level access scenario.

---

## 2. Broken Authentication

Tested:

- API access without JWT
- Invalid JWT
- Valid JWT

Without authentication:

```json
{
    "detail": "Authentication credentials were not provided."
}
```

Invalid JWT:

```json
{
    "detail": "Given token not valid for any token type"
}
```

Valid JWT successfully accessed the protected API.

### Result

Authentication protection was successfully verified.

---

## 3. Broken Object Property Level Authorization

Reviewed employee API response fields and serializers/permissions.

Sensitive authentication information such as passwords, password hashes, tokens, and database credentials was not exposed.

Employee-specific fields were reviewed for authorization and necessity.

---

## 4. Unrestricted Resource Consumption

Reviewed API throttling configuration.

Anonymous requests are limited to:

```text
10 requests/minute
```

Authenticated users are limited to:

```text
60 requests/minute
```

Repeated login testing confirmed HTTP `429 Too Many Requests`.

---

## 5. Security Misconfiguration

Reviewed:

- Debug configuration
- Secret management
- CORS
- CSRF
- Security middleware
- Throttling
- Environment configuration

A specific CORS origin is configured instead of allowing all origins.

Actual environment secrets are excluded from Git.

---

## 6. Improper Inventory Management

Reviewed the available API endpoints and authentication routes.

The current API structure and authentication endpoints were reviewed as part of the security assessment.

---

# Intentional Security Exercises

The following security scenarios were reviewed:

| Security Exercise                   | Result                                   |
| ----------------------------------- | ---------------------------------------- |
| Unauthorized employee object access | Tested and blocked                       |
| Sensitive field exposure            | Reviewed                                 |
| Permissive CORS                     | Reviewed and restricted                  |
| Missing login throttling            | Throttling implemented                   |
| Hard-coded secrets                  | Environment-based configuration reviewed |

Each exercise followed:

```text
Identify
   ↓
Explain Risk
   ↓
Fix / Configure
   ↓
Test
   ↓
Document
```

---

# Documentation Created

The following security documentation was created/updated:

```text
SECURITY_CHECKLIST.md
SECURITY_FINDINGS.md
CSRF_REVIEW.md
OWASP_API_SECURITY_REVIEW.md
.env.example
```

---

# Final Security Testing Summary

| Security Area                     | Status |
| --------------------------------- | ------ |
| Authentication without JWT        | PASS   |
| Invalid JWT                       | PASS   |
| Valid JWT                         | PASS   |
| Own employee authorization        | PASS   |
| BOLA / unauthorized object access | PASS   |
| Input validation                  | PASS   |
| SQL injection awareness           | PASS   |
| CORS review                       | PASS   |
| CSRF review                       | PASS   |
| Sensitive data exposure review    | PASS   |
| Rate limiting configuration       | PASS   |
| Rate limiting actual test         | PASS   |
| OWASP API Security Review         | PASS   |

---

# Final Outcome

SEC-004 — Django & API Security Hardening was reviewed across the required security areas.

The application security review covered authentication, authorization, secret management, CORS, CSRF, input validation, SQL injection awareness, sensitive data exposure, rate limiting, and OWASP API security concepts.

Final security testing was completed, including successful verification of JWT authentication, employee-level object authorization, and rate limiting with HTTP `429 Too Many Requests`.

