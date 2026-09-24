
# Database Indexes — DB-004

## 1. Objective

The objective of this task is to evaluate database indexes for commonly searched, filtered, ordered, and looked-up Employee fields.

The goal is to avoid unnecessary duplicate indexes and identify fields where indexing may be useful based on actual query usage.

---

## 2. Fields Evaluated

The following Employee fields were evaluated:

- `employee_code`
- `email`
- `department`
- `is_active`
- `joining_date`

---

## 3. Existing Index Configuration

The existing Django model configuration was reviewed.

### Employee Code

`employee_code` is unique.

```python
employee_code = models.CharField(
    max_length=20,
    unique=True
)
````

Because the field is unique, PostgreSQL already maintains a unique index for it.

No additional duplicate index is required.

---

### Email

`email` is unique.

```python
email = models.EmailField(
    unique=True
)
```

Because the field is unique, PostgreSQL already maintains a unique index for it.

No additional duplicate index is required.

---

### Department

The Employee → Department relationship uses a ForeignKey.

The ForeignKey already has an index:

```text
employees_employee_department_fk_id_f66e261d
```

Therefore, an additional duplicate index on the department foreign-key column is not required.

---

### Is Active

The `is_active` field was evaluated because it can commonly be used for filtering active employees.

```python
is_active = models.BooleanField(default=True)
```

Currently, no separate database index was added.

A Boolean field can have low selectivity because it normally contains only two values. Therefore, adding an index should depend on actual query patterns and table size rather than adding it blindly.

---

### Joining Date

The `joining_date` field was also evaluated because it may be used for filtering or ordering employees.

```python
joining_date = models.DateField()
```

Currently, no separate index was added.

An index on `joining_date` may become useful if the application frequently filters or orders a large number of employee records by joining date.

---

## 4. Existing PostgreSQL Indexes

The existing PostgreSQL indexes were inspected.

The following indexes were identified:

```text
employees_employee_pkey
employees_employee_employee_code_key
employees_employee_email_key
employees_employee_employee_code_fb9b0c8f_like
employees_employee_email_14fffd5e_like
employees_employee_department_fk_id_f66e261d
```

These indexes cover the primary key, unique employee code, email, and department foreign-key relationship.

---

## 5. Avoiding Duplicate Indexes

Duplicate indexes should not be added when Django/PostgreSQL already creates the required index.

The following fields already have appropriate index support:

* `id` — Primary key index
* `employee_code` — Unique index
* `email` — Unique index
* `department` — ForeignKey index

Therefore, additional duplicate indexes were not created for these fields.

---

## 6. PostgreSQL Query Plan Analysis

The following query was analyzed using PostgreSQL `EXPLAIN ANALYZE`:

```sql
EXPLAIN ANALYZE
SELECT *
FROM employees_employee
WHERE employee_code = 'EMP001';
```

The query plan returned:

```text
Seq Scan on employees_employee
(cost=0.00..1.38 rows=1 width=115)
(actual time=0.044..0.048 rows=1.00 loops=1)

Filter: ((employee_code)::text = 'EMP001'::text)

Rows Removed by Filter: 29

Planning Time: 7.151 ms
Execution Time: 0.076 ms
```

---

## 7. Query Plan Explanation

### Sequential Scan

PostgreSQL used a **Sequential Scan**.

This means PostgreSQL scanned the table rows to find the requested employee.

### Query Cost

The estimated cost was:

```text
0.00..1.38
```

### Rows

The query expected one matching row:

```text
rows=1
```

The actual result also contained one matching row.

### Execution Time

The measured execution time was:

```text
0.076 ms
```

### Why an Index Was Not Used

The Employee table currently contains only 30 records.

For such a small table, PostgreSQL can determine that scanning the complete table is cheaper than using an index.

Therefore, the Sequential Scan is expected for this small dataset and does not indicate a problem.

---

## 8. Indexing Decision

Based on the current application and dataset:

| Field           | Index Status      | Decision                                                    |
| --------------- | ----------------- | ----------------------------------------------------------- |
| `id`            | Primary key index | Existing index is sufficient                                |
| `employee_code` | Unique index      | Existing index is sufficient                                |
| `email`         | Unique index      | Existing index is sufficient                                |
| `department`    | ForeignKey index  | Existing index is sufficient                                |
| `is_active`     | No separate index | Evaluate based on query usage and table size                |
| `joining_date`  | No separate index | Consider for frequent filtering/ordering on larger datasets |

Indexes should be added based on actual query patterns and performance requirements rather than adding indexes to every field.

---

## 9. Conclusion

The existing PostgreSQL indexes were evaluated successfully.

Duplicate indexes were avoided because appropriate indexes already exist for the primary key, unique employee code, email, and department ForeignKey.

The `is_active` and `joining_date` fields were evaluated without blindly adding indexes.

The PostgreSQL `EXPLAIN ANALYZE` output was also reviewed. The test query used a Sequential Scan because the current Employee table contains only 30 records.

The database indexing evaluation for DB-004 was completed successfully.


