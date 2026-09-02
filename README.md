
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

```text
201 Created
```

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

````

