import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Employee REST API is running"


def test_get_all_employees(client):
    response = client.get("/employees")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_employee_not_found(client):
    response = client.get("/employees/99999")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Employee not found"


def test_create_employee_validation(client):
    response = client.post(
        "/employees",
        json={
            "name": "A",
            "email": "wrong-email",
            "department": "I",
            "salary": -5000
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Validation failed"