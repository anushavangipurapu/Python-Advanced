
# PostgreSQL Notes — Employee Management

## 1. Database

A database is a collection of related data.

Example:
The Employee Management application uses a PostgreSQL database named `employee_management`.

---

## 2. Schema

A schema is a logical container inside a PostgreSQL database.

Example:
The Django application stores its tables inside the PostgreSQL `public` schema.

---

## 3. Table

A table stores related data in rows and columns.

Example:
The Employee application has an `employees_employee` table.

---

## 4. Row

A row represents one record in a table.

Example:
One employee record represents one row in the employee table.

---

## 5. Column

A column represents one attribute or field of a record.

Example:
Employee table columns include:

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

---

## 6. Primary Key

A primary key uniquely identifies each row in a table.

Example:
The Employee model uses `id` as the primary key.

Each employee has a unique ID.

---

## 7. Foreign Key

A foreign key creates a relationship between two tables.

Example:
If an Employee belongs to a Department table, the Employee table can use a foreign key to reference the Department table.

---

## 8. Index

An index improves the speed of database searches.

Example:
An index can be useful when frequently searching employees by fields such as email or employee_code.

---

## 9. Constraint

A constraint controls the type and validity of data stored in a table.

Common constraints include:

- Primary Key
- Foreign Key
- Unique
- Not Null
- Check

Example:
Employee email and employee_code can be required to be unique.

---

## 10. Employee Management Database

Database name:

`employee_management`

Database user:

`employee_admin`

PostgreSQL default port:

`5432`

Django connects to PostgreSQL using environment variables:

- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

---

## 11. Django ORM Examples

Get all employees:

```python
Employee.objects.all()
````

Get active employees:

```python
Employee.objects.filter(is_active=True)
```

Get Backend employees:

```python
Employee.objects.filter(department="Backend")
```

Get employees ordered by highest salary:

```python
Employee.objects.order_by("-salary")
```

---

## 12. PostgreSQL Integration

The Django application was successfully configured to use PostgreSQL instead of SQLite.

Migrations were successfully applied.

30 Employee records were successfully created and verified using Django ORM.

CRUD operations were also tested successfully:

* Create
* Read
* Update
* Delete

PostgreSQL restart and Django reconnection were also tested successfully.

---

## 13. Environment Variables

Database credentials are stored in `.env`.

Example `.env.example`:

```env
DB_NAME=employee_management
DB_USER=employee_admin
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

The actual `.env` file is excluded from Git using `.gitignore`.

Never commit the real database password to Git
