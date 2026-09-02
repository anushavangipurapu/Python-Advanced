import logging

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import db
from models import Employee
from schemas import EmployeeSchema


employee_bp = Blueprint("employees", __name__)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


# CREATE EMPLOYEE
@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    try:
        data = employee_schema.load(
            request.get_json(silent=True) or {}
        )

        employee = Employee(
            name=data["name"],
            email=data["email"],
            department=data["department"],
            salary=data["salary"]
        )

        db.session.add(employee)
        db.session.commit()

        logging.info("Employee created: %s", employee.id)

        return jsonify(employee.to_dict()), 201

    except ValidationError as error:
        return jsonify({
            "error": "Validation failed",
            "details": error.messages
        }), 400

    except IntegrityError:
        db.session.rollback()

        return jsonify({
            "error": "Email already exists"
        }), 409

    except SQLAlchemyError:
        db.session.rollback()
        logging.exception("Database error while creating employee")

        return jsonify({
            "error": "Database error"
        }), 500


# GET ALL EMPLOYEES
@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    try:
        employees = Employee.query.all()

        return jsonify(
            employees_schema.dump(employees)
        ), 200

    except SQLAlchemyError:
        logging.exception("Database error while fetching employees")

        return jsonify({
            "error": "Database error"
        }), 500


# GET SINGLE EMPLOYEE
@employee_bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    try:
        employee = db.session.get(Employee, employee_id)

        if employee is None:
            return jsonify({
                "error": "Employee not found"
            }), 404

        return jsonify(employee.to_dict()), 200

    except SQLAlchemyError:
        logging.exception("Database error while fetching employee")

        return jsonify({
            "error": "Database error"
        }), 500


# UPDATE EMPLOYEE - PUT
@employee_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    try:
        employee = db.session.get(Employee, employee_id)

        if employee is None:
            return jsonify({
                "error": "Employee not found"
            }), 404

        data = employee_schema.load(
            request.get_json(silent=True) or {}
        )

        employee.name = data["name"]
        employee.email = data["email"]
        employee.department = data["department"]
        employee.salary = data["salary"]

        db.session.commit()

        logging.info("Employee updated: %s", employee.id)

        return jsonify(employee.to_dict()), 200

    except ValidationError as error:
        return jsonify({
            "error": "Validation failed",
            "details": error.messages
        }), 400

    except IntegrityError:
        db.session.rollback()

        return jsonify({
            "error": "Email already exists"
        }), 409

    except SQLAlchemyError:
        db.session.rollback()
        logging.exception("Database error while updating employee")

        return jsonify({
            "error": "Database error"
        }), 500


# PARTIAL UPDATE - PATCH
@employee_bp.route("/employees/<int:employee_id>", methods=["PATCH"])
def patch_employee(employee_id):
    try:
        employee = db.session.get(Employee, employee_id)

        if employee is None:
            return jsonify({
                "error": "Employee not found"
            }), 404

        data = EmployeeSchema(
            partial=True
        ).load(
            request.get_json(silent=True) or {}
        )

        for field, value in data.items():
            setattr(employee, field, value)

        db.session.commit()

        logging.info("Employee partially updated: %s", employee.id)

        return jsonify(employee.to_dict()), 200

    except ValidationError as error:
        return jsonify({
            "error": "Validation failed",
            "details": error.messages
        }), 400

    except IntegrityError:
        db.session.rollback()

        return jsonify({
            "error": "Email already exists"
        }), 409

    except SQLAlchemyError:
        db.session.rollback()
        logging.exception("Database error while patching employee")

        return jsonify({
            "error": "Database error"
        }), 500


# DELETE EMPLOYEE
@employee_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        employee = db.session.get(Employee, employee_id)

        if employee is None:
            return jsonify({
                "error": "Employee not found"
            }), 404

        db.session.delete(employee)
        db.session.commit()

        logging.info("Employee deleted: %s", employee.id)

        return jsonify({
            "message": "Employee deleted successfully"
        }), 200

    except SQLAlchemyError:
        db.session.rollback()
        logging.exception("Database error while deleting employee")

        return jsonify({
            "error": "Database error"
        }), 500