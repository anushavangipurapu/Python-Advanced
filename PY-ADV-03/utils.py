def clean_name(name):
    return name.strip().title()


def is_valid_email(email):
    return "@" in email and "." in email


def create_user_record(name, email, city):
    return {
        "name": clean_name(name),
        "email": email,
        "city": city
    }
  