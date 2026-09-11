import logging

from app.models.student import Student
from app.exceptions.student_exceptions import StudentNotFoundError
from app.utils.validators import (
    validate_student_age,
    validate_student_course,
    validate_student_name,
)


logger = logging.getLogger(__name__)


class StudentService:
    """Handle student business logic."""

    def __init__(self) -> None:
        """Initialize the student service."""

        self.students: dict[int, Student] = {}
        self.next_student_id = 1

    def create_student(
        self,
        name: str,
        age: int,
        course: str,
    ) -> Student:
        """Create a new student."""

        validate_student_name(name)
        validate_student_age(age)
        validate_student_course(course)

        student = Student(
            student_id=self.next_student_id,
            name=name.strip(),
            age=age,
            course=course.strip(),
        )

        self.students[student.student_id] = student
        self.next_student_id += 1

        logger.info(
            "Student created: %s",
            student.student_id,
        )

        return student

    def get_student(self, student_id: int) -> Student:
        """Get a student by ID."""

        if student_id not in self.students:
            raise StudentNotFoundError("Student not found.")

        return self.students[student_id]

    def update_student(
        self,
        student_id: int,
        name: str,
        age: int,
        course: str,
    ) -> Student:
        """Update an existing student."""

        validate_student_name(name)
        validate_student_age(age)
        validate_student_course(course)

        student = self.get_student(student_id)

        student.update(
            name=name.strip(),
            age=age,
            course=course.strip(),
        )

        logger.info("Student updated: %s", student_id)

        return student

    def delete_student(self, student_id: int) -> None:
        """Delete a student."""

        self.get_student(student_id)

        del self.students[student_id]

        logger.info("Student deleted: %s", student_id)

    def search_students(
        self,
        search_text: str,
    ) -> list[Student]:
        """Search students by name or course."""

        search_text = search_text.strip().lower()

        return [
            student
            for student in self.students.values()
            if (
                search_text in student.name.lower()
                or search_text in student.course.lower()
            )
        ]

    def get_all_students(self) -> list[Student]:
        """Return all students."""

        return list(self.students.values())