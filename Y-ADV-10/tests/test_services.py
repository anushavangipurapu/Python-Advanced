import pytest
from flask import Flask

from app.models import db
from app.services import (
    create_employee,
    get_employee,
    get_all_employees,
    update_employee,
    delete_employee
)
from app.exceptions import EmployeeNotFoundError


@pytest.fixture
def app():
    app = Flask(__name__)

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


def test_create_employee(app):
    with app.app_context():
        employee = create_employee({
            "name": "Test User",
            "department": "IT",
            "salary": 50000,
            "age": 25,
            "city": "Hyderabad"
        })

        assert employee.id is not None
        assert employee.name == "Test User"
        assert employee.department == "IT"


def test_get_employee(app):
    with app.app_context():
        employee = create_employee({
            "name": "Ravi",
            "department": "HR",
            "salary": 45000,
            "age": 28,
            "city": "Hyderabad"
        })

        result = get_employee(employee.id)

        assert result.name == "Ravi"


def test_get_all_employees(app):
    with app.app_context():
        create_employee({
            "name": "Ravi",
            "department": "IT",
            "salary": 45000,
            "age": 28,
            "city": "Hyderabad"
        })

        create_employee({
            "name": "Anu",
            "department": "HR",
            "salary": 50000,
            "age": 26,
            "city": "Chennai"
        })

        employees = get_all_employees()

        assert len(employees) == 2


def test_update_employee(app):
    with app.app_context():
        employee = create_employee({
            "name": "Ravi",
            "department": "IT",
            "salary": 45000,
            "age": 28,
            "city": "Hyderabad"
        })

        updated = update_employee(
            employee.id,
            {
                "name": "Ravi Updated",
                "salary": 55000
            }
        )

        assert updated.name == "Ravi Updated"
        assert updated.salary == 55000


def test_delete_employee(app):
    with app.app_context():
        employee = create_employee({
            "name": "Test Delete",
            "department": "IT",
            "salary": 40000,
            "age": 25,
            "city": "Hyderabad"
        })

        employee_id = employee.id

        delete_employee(employee_id)

        with pytest.raises(EmployeeNotFoundError):
            get_employee(employee_id)