# Employee Management REST API v2 - API Documentation

**Date:** 18-Sep-2026

**Project:** Employee Management Backend

**Technology:** Django + Django REST Framework + PostgreSQL

---

# Employee Management REST API v2 — API Documentation

## Overview

The Employee Management REST API v2 is built using Django and Django REST Framework.

The API provides employee CRUD operations, validation, filtering, searching, ordering, pagination, and standardized error handling.

---

## Base URL

```text
http://127.0.0.1:8000/api/v1/
````

## Authentication

Authentication is not required for the current API configuration.

---

# 1. Get All Employees

## Endpoint

```text
GET /api/v1/employees/
```

## HTTP Method

```text
GET
```

## Authentication

Not required.

## Request Parameters

Optional query parameters:

* `page` — Page number
* `department` — Filter by department
* `is_active` — Filter by active status
* `salary_min` — Minimum salary
* `search` — Search employees
* `ordering` — Sort employees

## Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/
```

## Success Response

**Status Code:** `200 OK`

```json
{
    "count": 30,
    "next": "http://127.0.0.1:8000/api/v1/employees/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "employee_code": "EMP001",
            "first_name": "Divya",
            "last_name": "Kumar",
            "email": "divya@example.com"
        }
    ]
}
```

---

# 2. Create Employee

## Endpoint

```text
POST /api/v1/employees/
```

## HTTP Method

```text
POST
```

## Authentication

Not required.

## Request Body

```json
{
    "employee_code": "EMP101",
    "first_name": "Anusha",
    "last_name": "V",
    "email": "anusha101@example.com",
    "phone": "9876543210",
    "department": "Backend",
    "designation": "Python Developer",
    "salary": 70000,
    "joining_date": "2025-01-15",
    "is_active": true
}
```

## Success Response

**Status Code:** `201 Created`

```json
{
    "id": 42,
    "employee_code": "EMP101",
    "first_name": "Anusha",
    "last_name": "V",
    "email": "anusha101@example.com",
    "phone": "9876543210",
    "department": "Backend",
    "designation": "Python Developer",
    "salary": "70000.00",
    "joining_date": "2025-01-15",
    "is_active": true
}
```

## Error Response

**Status Code:** `400 Bad Request`

```json
{
    "email": [
        "Email already exists."
    ]
}
```

---

# 3. Get Employee Detail

## Endpoint

```text
GET /api/v1/employees/{id}/
```

## HTTP Method

```text
GET
```

## Authentication

Not required.

## Request Parameter

* `id` — Employee ID

## Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/1/
```

## Success Response

**Status Code:** `200 OK`

```json
{
    "id": 1,
    "employee_code": "EMP001",
    "first_name": "Divya",
    "last_name": "Kumar",
    "email": "divya@example.com"
}
```

## Error Response

**Status Code:** `404 Not Found`

```json
{
    "detail": "Employee not found."
}
```

---

# 4. Update Employee

## Endpoint

```text
PUT /api/v1/employees/{id}/
```

## HTTP Method

```text
PUT
```

## Authentication

Not required.

## Request Parameter

* `id` — Employee ID

## Request Body

```json
{
    "employee_code": "EMP001",
    "first_name": "Divya",
    "last_name": "Updated",
    "email": "divya@example.com",
    "phone": "9876543210",
    "department": "IT",
    "designation": "Developer",
    "salary": 75000,
    "joining_date": "2025-01-15",
    "is_active": true
}
```

## Success Response

**Status Code:** `200 OK`

```json
{
    "id": 1,
    "employee_code": "EMP001",
    "first_name": "Divya",
    "last_name": "Updated"
}
```

## Error Response

**Status Code:** `400 Bad Request`

```json
{
    "salary": [
        "Salary cannot be negative."
    ]
}
```

---

# 5. Partial Update Employee

## Endpoint

```text
PATCH /api/v1/employees/{id}/
```

## HTTP Method

```text
PATCH
```

## Authentication

Not required.

## Request Parameter

* `id` — Employee ID

## Request Body

Only the fields that need to be changed are required.

Example:

```json
{
    "salary": 80000
}
```

## Success Response

**Status Code:** `200 OK`

```json
{
    "id": 1,
    "employee_code": "EMP001",
    "salary": "80000.00"
}
```

## Error Response

**Status Code:** `400 Bad Request`

```json
{
    "salary": [
        "Salary cannot be negative."
    ]
}
```

---

# 6. Delete Employee

## Endpoint

```text
DELETE /api/v1/employees/{id}/
```

## HTTP Method

```text
DELETE
```

## Authentication

Not required.

## Request Parameter

* `id` — Employee ID

## Example Request

```text
DELETE http://127.0.0.1:8000/api/v1/employees/1/
```

## Success Response

**Status Code:** `204 No Content`

```text
No response body
```

## Error Response

**Status Code:** `404 Not Found`

```json
{
    "detail": "Employee not found."
}
```

---

# 7. Get Active Employees

## Endpoint

```text
GET /api/v1/employees/active/
```

## HTTP Method

```text
GET
```

## Authentication

Not required.

## Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/active/
```

## Success Response

**Status Code:** `200 OK`

```json
[
    {
        "id": 1,
        "employee_code": "EMP001",
        "first_name": "Divya",
        "is_active": true
    }
]
```

---

# 8. Filtering

## Department Filter

### Endpoint

```text
GET /api/v1/employees/?department=Backend
```

### Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/?department=Backend
```

Returns employees from the Backend department.

## Active Status Filter

### Endpoint

```text
GET /api/v1/employees/?is_active=true
```

### Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/?is_active=true
```

Returns active employees.

## Minimum Salary Filter

### Endpoint

```text
GET /api/v1/employees/?salary_min=60000
```

### Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/?salary_min=60000
```

Returns employees whose salary is greater than or equal to 60000.

## Success Response

**Status Code:** `200 OK`

```json
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": []
}
```

---

# 9. Search Employees

## Endpoint

```text
GET /api/v1/employees/?search={value}
```

## HTTP Method

```text
GET
```

## Authentication

Not required.

## Search Fields

The following fields can be searched:

* First name
* Last name
* Email
* Employee code
* Department

## Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/?search=Divya
```

## Success Response

**Status Code:** `200 OK`

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "employee_code": "EMP001",
            "first_name": "Divya",
            "last_name": "Kumar"
        }
    ]
}
```

---

# 10. Ordering

## Salary Ascending

```text
GET /api/v1/employees/?ordering=salary
```

## Salary Descending

```text
GET /api/v1/employees/?ordering=-salary
```

## Joining Date

```text
GET /api/v1/employees/?ordering=joining_date
```

## Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/?ordering=-salary
```

## Success Response

**Status Code:** `200 OK`

```json
{
    "count": 30,
    "next": null,
    "previous": null,
    "results": []
}
```

---

# 11. Pagination

## Page 1

```text
GET /api/v1/employees/?page=1
```

## Page 2

```text
GET /api/v1/employees/?page=2
```

## Page Size

The configured page size is:

```text
5 employees per page
```

## Example Request

```text
GET http://127.0.0.1:8000/api/v1/employees/?page=1
```

## Success Response

**Status Code:** `200 OK`

```json
{
    "count": 30,
    "next": "http://127.0.0.1:8000/api/v1/employees/?page=2",
    "previous": null,
    "results": []
}
```

## Pagination Response Fields

* `count` — Total number of employees
* `next` — URL for the next page
* `previous` — URL for the previous page
* `results` — Employees in the current page

---

# 12. Validation Rules

## Employee Code

* Required
* Unique
* Must start with `EMP`
* Must contain numbers after `EMP`

## Email

* Required
* Must be a valid email address
* Must be unique

## Salary

* Cannot be negative
* Cannot exceed `10000000`

## Joining Date

* Must be a valid date
* Cannot be a future date

## Phone

* Must contain exactly 10 digits

---

# 13. Standard API Errors

## Validation Error

**Status Code:** `400 Bad Request`

Example:

```json
{
    "email": [
        "Email already exists."
    ]
}
```

## Employee Not Found

**Status Code:** `404 Not Found`

Example:

```json
{
    "detail": "Employee not found."
}
```

---

# 14. HTTP Status Codes

| Status Code | Meaning     |
| ----------- | ----------- |
| 200         | OK          |
| 201         | Created     |
| 204         | No Content  |
| 400         | Bad Request |
| 404         | Not Found   |

---

# 15. API Testing

The Employee API was tested using:

* PowerShell
* Pytest
* Manual API requests

Automated test result:

```text
15 passed
```

The API was also tested for CRUD operations, validation, filtering, search, ordering, pagination, and error handling.

---

# 16. API Features

The Employee Management REST API v2 provides:

* Django
* Django REST Framework
* Serializers
* ViewSets
* Routers
* CRUD operations
* Validation
* Filtering
* Searching
* Ordering
* Pagination
* Standardized error handling
* API testing
* Debugging
* Code review

---

# 17. API Request Flow

```text
HTTP Request
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

# 18. Project Status

Employee Management REST API v2 has completed:

* DRF configuration
* Serializers
* API Views
* ViewSets
* Routers
* CRUD operations
* Validation
* Filtering
* Searching
* Ordering
* Pagination
* Error handling
* API testing
* Debugging
* Code review
* API documentation


