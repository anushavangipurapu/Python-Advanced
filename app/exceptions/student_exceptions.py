class StudentManagementError(Exception):
    """Base exception for student management errors."""


class StudentNotFoundError(StudentManagementError):
    """Raised when a student is not found."""


class DuplicateStudentError(StudentManagementError):
    """Raised when a student ID already exists."""


class InvalidStudentDataError(StudentManagementError):
    """Raised when student data is invalid."""