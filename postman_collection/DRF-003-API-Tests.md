# DRF-003 API Test Collection

## Base URL

http://127.0.0.1:8000/api/v1/

## 1. Employee List

### GET - List Employees

GET /employees/

Expected Status: 200 OK

---

## 2. Employee Create

### POST - Create Employee

POST /employees/

Expected Status: 201 Created

---

## 3. Employee Detail

### GET - Retrieve Employee

GET /employees/1/

Expected Status: 200 OK

---

## 4. Employee Update

### PUT - Full Update

PUT /employees/1/

Expected Status: 200 OK

---

## 5. Employee Partial Update

### PATCH - Partial Update

PATCH /employees/1/

Expected Status: 200 OK

---

## 6. Employee Delete

### DELETE - Delete Employee

DELETE /employees/1/

Expected Status: 204 No Content

---

## 7. Active Employees

### GET - Active Employees

GET /employees/active/

Expected Status: 200 OK

---

## 8. Department Filter

### GET - Backend Employees

GET /employees/?department=Backend

Expected Status: 200 OK

---

## 9. Active Filter

### GET - Active Employees Filter

GET /employees/?is_active=true

Expected Status: 200 OK

---

## 10. Salary Filter

### GET - Minimum Salary

GET /employees/?salary_min=60000

Expected Status: 200 OK

---

## 11. Search

### GET - Search Employee

GET /employees/?search=Divya

Expected Status: 200 OK

---

## 12. Salary Ordering

### GET - Salary Ascending

GET /employees/?ordering=salary

Expected Status: 200 OK

### GET - Salary Descending

GET /employees/?ordering=-salary

Expected Status: 200 OK

---

## 13. Joining Date Ordering

### GET - Joining Date

GET /employees/?ordering=joining_date

Expected Status: 200 OK

---

## 14. Invalid Ordering Field

### GET - Invalid Ordering

GET /employees/?ordering=wrongfield

Expected Status: 200 OK

---

## 15. Combined Filters

### GET - Department + Active + Salary Ordering

GET /employees/?department=Backend&is_active=true&ordering=-salary

Expected Status: 200 OK

---

## Test Result

All DRF-003 API endpoints and filtering, searching, and ordering scenarios were tested successfully.