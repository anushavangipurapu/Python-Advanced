

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

