from app.exceptions.student_exceptions import (
    InvalidStudentDataError,
)


def validate_student_name(name: str) -> None:
    """Validate the student name."""

    if not name or not name.strip():
        raise InvalidStudentDataError(
            "Student name cannot be empty."
        )


def validate_student_age(age: int) -> None:
    """Validate the student age."""

    if age < 5 or age > 100:
        raise InvalidStudentDataError(
            "Student age must be between 5 and 100."
        )


def validate_student_course(course: str) -> None:
    """Validate the student course."""

    if not course or not course.strip():
        raise InvalidStudentDataError(
            "Student course cannot be empty."
        )