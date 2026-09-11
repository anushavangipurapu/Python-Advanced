import logging

from app.config.settings import setup_logging
from app.services.student_service import StudentService


def main() -> None:
    """Run the Student Management System."""

    setup_logging()

    logger = logging.getLogger(__name__)

    service = StudentService()

    student = service.create_student(
        name="Anusha",
        age=20,
        course="Python",
    )

    logger.info(
        "Student created successfully: %s",
        student.to_dict(),
    )

    print("Student Management System")
    print(student.to_dict())


if __name__ == "__main__":
    main()