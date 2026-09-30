# SEC-003 — Role-Based Access Control & Permissions

## Objective

Implement role-based authorization so different users can perform different operations.

## Roles

### ADMIN

- Can manage all employee information.
- Can create employees.
- Can update employees.
- Can delete employees.
- Can view employee information.

### HR

- Can manage employee information.
- Can create employees.
- Can update employees.
- Can view employee information.
- Cannot delete employees.

### MANAGER

- Can view permitted employees.
- Can manage employees within the permitted business scope.
- Cannot delete employees.

### EMPLOYEE

- Can access their own permitted information.
- Cannot access other employees' information.
- Cannot create employees.
- Cannot update other employees.
- Cannot delete employees.

## Role Summary

ADMIN → Full access

HR → Employee management access

MANAGER → Permitted employee access

EMPLOYEE → Own information access