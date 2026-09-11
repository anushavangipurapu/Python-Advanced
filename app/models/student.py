class Student:
    """Represent a student."""

    def __init__(
        self,
        student_id: int,
        name: str,
        age: int,
        course: str,
    ) -> None:
        """Create a student."""

        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def update(
        self,
        name: str,
        age: int,
        course: str,
    ) -> None:
        """Update student details."""

        self.name = name
        self.age = age
        self.course = course

    def to_dict(self) -> dict:
        """Convert student data to a dictionary."""

        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
        }