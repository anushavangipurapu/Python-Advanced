def validate_employee(data):
    required_fields = [
        "name",
        "department",
        "salary",
        "age",
        "city"
    ]

    for field in required_fields:
        if field not in data:
            return f"{field} is required"

    if not isinstance(data["name"], str) or not data["name"].strip():
        return "Name cannot be empty"

    if not isinstance(data["department"], str) or not data["department"].strip():
        return "Department cannot be empty"

    if not isinstance(data["city"], str) or not data["city"].strip():
        return "City cannot be empty"

    if not isinstance(data["salary"], (int, float)):
        return "Salary must be a number"

    if data["salary"] < 0:
        return "Salary cannot be negative"

    if not isinstance(data["age"], int):
        return "Age must be an integer"

    if data["age"] <= 0:
        return "Age must be greater than 0"

    return None