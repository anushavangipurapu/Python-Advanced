# Y-ADV-10 — Python Employee Management Platform

## Project Overview

The Python Employee Management Platform is a Flask-based REST API application for managing employee information.

The project demonstrates Python programming, REST APIs, database operations, validation, exception handling, logging, unit testing, and Pandas-based data analysis.

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Pandas
* Pytest
* SQLAlchemy
* Git

## Features

1. Create employee
2. Update employee
3. Delete employee
4. Search employee
5. List all employees
6. Store employee data in SQLite database
7. Expose REST APIs using Flask
8. Validate API requests
9. Handle application exceptions
10. Add application logging
11. Write unit tests
12. Read employee data using Pandas
13. Generate employee statistics
14. Maintain a clean project structure

## Project Structure

```text
Y-ADV-10/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── validation.py
│   ├── services.py
│   ├── routes.py
│   ├── exceptions.py
│   └── logging_config.py
│
├── analysis/
│   └── employee_analysis.py
│
├── data/
│
├── tests/
│   └── test_services.py
│
├── instance/
│   └── employees.db
│
├── venv/
│
├── run.py
└── README.md
```

## Installation

First, create a virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install flask flask-sqlalchemy pandas pytest
```

## Run the Application

Start the Flask application:

```powershell
python .\run.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

## REST API Endpoints

### 1. Create Employee

Create a new employee:

```text
POST /employees
```

Example request:

```json
{
    "name": "Ravi",
    "department": "IT",
    "salary": 45000,
    "age": 28,
    "city": "Hyderabad"
}
```

### 2. List Employees

Retrieve all employees from the database:

```text
GET /employees
```

### 3. Get Employee

Retrieve a specific employee:

```text
GET /employees/<employee_id>
```

Example:

```text
GET /employees/1
```

### 4. Update Employee

Update an existing employee:

```text
PUT /employees/<employee_id>
```

Example request:

```json
{
    "salary": 50000,
    "city": "Hyderabad"
}
```

### 5. Delete Employee

Delete an employee:

```text
DELETE /employees/<employee_id>
```

Example:

```text
DELETE /employees/1
```

### 6. Search Employee

Search for an employee by name:

```text
GET /employees/search?name=Ravi
```

## API Validation

The application validates employee data before creating or updating records.

The following validations are implemented:

* Name cannot be empty
* Department cannot be empty
* City cannot be empty
* Salary must be a number
* Salary cannot be negative
* Age must be an integer
* Age must be greater than zero

### Invalid Salary Example

Request:

```json
{
    "salary": -5000
}
```

Response:

```json
{
    "error": "Salary cannot be negative"
}
```

Both Create and Update APIs support request validation.

## Exception Handling

Custom exception handling is implemented for employee-related errors.

Custom exception:

```text
EmployeeNotFoundError
```

If an employee does not exist, the API returns:

```text
404 Not Found
```

## Logging

Application logging is implemented using Python's `logging` module.

Logs are generated when employee operations are performed.

Example logs:

```text
INFO - Fetching all employees
INFO - Total employees found: 1
INFO - Employee created successfully
INFO - Employee updated successfully
INFO - Employee deleted successfully
```

Logging helps track application operations and API requests.

## Unit Testing

Unit tests are implemented using Pytest.

Run the tests using:

```powershell
python -m pytest -q
```

Current test result:

```text
5 passed
```

All 5 unit tests passed successfully.

## Pandas Data Analysis

Employee data is read from the SQLite database using Pandas.

The following employee statistics are generated:

* Total Employees
* Average Salary
* Average Age
* Highest Salary
* Lowest Salary

Run the analysis using:

```powershell
python .\analysis\employee_analysis.py
```

Example output:

```text
Employee Statistics:
Total Employees: 1
Average Salary: 45000.0
Average Age: 28.0
Highest Salary: 45000.0
Lowest Salary: 45000.0
```

## Database

Employee information is stored in a SQLite database.

Database location:

```text
instance/employees.db
```

The Employee table contains the following fields:

* id
* name
* department
* salary
* age
* city

## Completed Tasks

The following Y-ADV-10 tasks have been completed:

1. Create Employee ✅
2. Update Employee ✅
3. Delete Employee ✅
4. Search Employee ✅
5. List Employees ✅
6. Store Employees in Database ✅
7. Expose REST APIs ✅
8. Validate API Requests ✅
9. Handle Exceptions ✅
10. Add Logging ✅
11. Write Unit Tests ✅
12. Read Employee Data using Pandas ✅
13. Generate Employee Statistics ✅
14. Create Clean Project Structure ✅
15. Create README Documentation ✅

## Conclusion

The Y-ADV-10 — Python Employee Management Platform has been successfully implemented.

The project integrates Flask REST APIs, SQLite database operations, CRUD functionality, API validation, exception handling, logging, unit testing, and Pandas-based data analysis.

The project is ready to be committed and pushed to the Git repository.
