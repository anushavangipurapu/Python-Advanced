import logging

from .models import db, Employee
from .exceptions import EmployeeNotFoundError


logger = logging.getLogger(__name__)


def create_employee(data):
    logger.info("Creating employee: %s", data["name"])

    employee = Employee(
        name=data["name"],
        department=data["department"],
        salary=data["salary"],
        age=data["age"],
        city=data["city"]
    )

    db.session.add(employee)
    db.session.commit()

    logger.info(
        "Employee created successfully: ID=%s, Name=%s",
        employee.id,
        employee.name
    )

    return employee


def get_all_employees():
    logger.info("Fetching all employees")

    employees = Employee.query.all()

    logger.info("Total employees found: %s", len(employees))

    return employees


def get_employee(employee_id):
    logger.info("Fetching employee with ID=%s", employee_id)

    employee = db.session.get(Employee, employee_id)

    if employee is None:
        logger.error("Employee not found: ID=%s", employee_id)
        raise EmployeeNotFoundError("Employee not found")

    logger.info(
        "Employee found: ID=%s, Name=%s",
        employee.id,
        employee.name
    )

    return employee


def update_employee(employee_id, data):
    logger.info("Updating employee: ID=%s", employee_id)

    employee = get_employee(employee_id)

    employee.name = data.get("name", employee.name)
    employee.department = data.get("department", employee.department)
    employee.salary = data.get("salary", employee.salary)
    employee.age = data.get("age", employee.age)
    employee.city = data.get("city", employee.city)

    db.session.commit()

    logger.info(
        "Employee updated successfully: ID=%s, Name=%s",
        employee.id,
        employee.name
    )

    return employee


def delete_employee(employee_id):
    logger.info("Deleting employee: ID=%s", employee_id)

    employee = get_employee(employee_id)

    db.session.delete(employee)
    db.session.commit()

    logger.info(
        "Employee deleted successfully: ID=%s",
        employee_id
    )