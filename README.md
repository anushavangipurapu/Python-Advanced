

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
