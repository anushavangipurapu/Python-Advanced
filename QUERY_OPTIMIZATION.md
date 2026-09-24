
# Query Optimization — DB-004

## 1. Objective

The objective of this task is to identify and optimize inefficient database queries in the Employee Management API.

The main focus was identifying the N+1 query problem and optimizing related-object loading using Django ORM.

---

## 2. N+1 Query Problem

The N+1 query problem occurs when one query is used to retrieve the main objects and additional queries are executed repeatedly for related objects.

For example:

```python
employees = Employee.objects.all()

for employee in employees:
    print(employee.employee_code, employee.department.name)
````

For 30 employees, this resulted in:

```text
31 queries
```

This included:

* 1 query to retrieve employees
* 30 additional queries to retrieve departments

---

## 3. Using select_related()

The Employee → Department and Employee → EmployeeProfile relationships were optimized using `select_related()`.

```python
employees = Employee.objects.select_related(
    "department",
    "profile"
)
```

The query count was reduced from:

```text
31 queries → 1 query
```

`select_related()` performs a SQL JOIN and loads related ForeignKey and OneToOne objects together.

---

## 4. Using prefetch_related()

The Employee → Project ManyToMany relationship was optimized using `prefetch_related()`.

```python
employees = Employee.objects.prefetch_related("projects")

for employee in employees:
    employee.projects.all()
```

The query count was:

```text
2 queries
```

`prefetch_related()` performs a separate query for the related objects and combines them in Django.

---

## 5. Combined Optimization

The Employee details endpoint was optimized using both methods:

```python
employees = (
    Employee.objects
    .select_related("department", "profile")
    .prefetch_related("projects")
)
```

The endpoint returns:

* Employee details
* Department
* Employee Profile
* Projects

---

## 6. Performance Comparison

Before optimization:

```text
Query Count: 91
```

After optimization:

```text
Query Count: 2
```

Therefore, the database query count was reduced from:

```text
91 queries → 2 queries
```

This significantly reduced unnecessary database queries.

---

## 7. API Verification

Endpoint:

```text
GET /api/employees/details/
```

Test result:

```text
Status: 200
Query Count: 2
```

The API response was successfully returned after optimization.

---

## 8. Final Optimized Queryset

```python
Employee.objects.select_related(
    "department",
    "profile"
).prefetch_related("projects")
```

This avoids unnecessary repeated queries while maintaining the same API response data.

---

## 9. Conclusion

The N+1 query problem was identified and optimized successfully.

Django's `select_related()` was used for ForeignKey and OneToOne relationships, while `prefetch_related()` was used for the ManyToMany relationship.

The final query count was reduced from 91 queries to 2 queries, and the API continued to return a successful 200 response.

