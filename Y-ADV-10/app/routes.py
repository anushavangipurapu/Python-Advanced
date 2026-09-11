from flask import Blueprint, request, jsonify

from .models import Employee
from .services import (
    create_employee,
    get_all_employees,
    get_employee,
    update_employee,
    delete_employee
)
from .validation import validate_employee
from .exceptions import EmployeeNotFoundError


employee_bp = Blueprint(
    "employees",
    __name__,
    url_prefix="/employees"
)


# CREATE EMPLOYEE
@employee_bp.route("", methods=["POST"])
def create():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    error = validate_employee(data)

    if error:
        return jsonify({
            "error": error
        }), 400

    employee = create_employee(data)

    return jsonify(employee.to_dict()), 201


# LIST ALL EMPLOYEES
@employee_bp.route("", methods=["GET"])
def list_employees():
    employees = get_all_employees()

    return jsonify([
        employee.to_dict()
        for employee in employees
    ]), 200


# GET SINGLE EMPLOYEE
@employee_bp.route("/<int:employee_id>", methods=["GET"])
def get(employee_id):
    try:
        employee = get_employee(employee_id)

        return jsonify(employee.to_dict()), 200

    except EmployeeNotFoundError as error:
        return jsonify({
            "error": str(error)
        }), 404


# UPDATE EMPLOYEE
@employee_bp.route("/<int:employee_id>", methods=["PUT"])
def update(employee_id):
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    try:
        employee = get_employee(employee_id)

        updated_data = {
            "name": data.get("name", employee.name),
            "department": data.get("department", employee.department),
            "salary": data.get("salary", employee.salary),
            "age": data.get("age", employee.age),
            "city": data.get("city", employee.city)
        }

        error = validate_employee(updated_data)

        if error:
            return jsonify({
                "error": error
            }), 400

        employee = update_employee(employee_id, data)

        return jsonify(employee.to_dict()), 200

    except EmployeeNotFoundError as error:
        return jsonify({
            "error": str(error)
        }), 404


# DELETE EMPLOYEE
@employee_bp.route("/<int:employee_id>", methods=["DELETE"])
def delete(employee_id):
    try:
        delete_employee(employee_id)

        return jsonify({
            "message": "Employee deleted successfully"
        }), 200

    except EmployeeNotFoundError as error:
        return jsonify({
            "error": str(error)
        }), 404


# SEARCH EMPLOYEE
@employee_bp.route("/search", methods=["GET"])
def search():
    name = request.args.get("name", "")

    employees = Employee.query.filter(
        Employee.name.ilike(f"%{name}%")
    ).all()

    return jsonify([
        employee.to_dict()
        for employee in employees
    ]), 200