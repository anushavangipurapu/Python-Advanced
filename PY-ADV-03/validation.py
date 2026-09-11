def validate_user(user):

    required_fields = ["name", "email", "address"]

    for field in required_fields:

        if field not in user:
            return False

    if "city" not in user["address"]:
        return False

    return True