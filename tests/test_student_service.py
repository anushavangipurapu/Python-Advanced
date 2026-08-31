import pytest

from app.services.student_service import StudentService
from app.exceptions.student_exceptions import StudentNotFoundError


def test_create_student():
    """Test student creation."""

    service = StudentService()

    student = service.create_student(
        name="Anusha",
        age=20,
        course="Python",
    )

    assert student.student_id == 1
    assert student.name == "Anusha"
    assert student.age == 20
    assert student.course == "Python"


def test_get_student():
    """Test getting a student."""

    service = StudentService()

    created_student = service.create_student(
        name="Anusha",
        age=20,
        course="Python",
    )

    student = service.get_student(created_student.student_id)

    assert student.name == "Anusha"


def test_update_student():
    """Test updating a student."""

    service = StudentService()

    student = service.create_student(
        name="Anusha",
        age=20,
        course="Python",
    )

    updated_student = service.update_student(
        student.student_id,
        name="Anusha Updated",
        age=21,
        course="Django",
    )

    assert updated_student.name == "Anusha Updated"
    assert updated_student.age == 21
    assert updated_student.course == "Django"


def test_delete_student():
    """Test deleting a student."""

    service = StudentService()

    student = service.create_student(
        name="Anusha",
        age=20,
        course="Python",
    )

    service.delete_student(student.student_id)

    with pytest.raises(StudentNotFoundError):
        service.get_student(student.student_id)


def test_search_students():
    """Test student search."""

    service = StudentService()

    service.create_student(
        name="Anusha",
        age=20,
        course="Python",
    )

    service.create_student(
        name="Ravi",
        age=22,
        course="Java",
    )

    results = service.search_students("Anusha")

    assert len(results) == 1
    assert results[0].name == "Anusha"


def test_student_not_found():
    """Test student not found exception."""

    service = StudentService()

    with pytest.raises(StudentNotFoundError):
        service.get_student(999)