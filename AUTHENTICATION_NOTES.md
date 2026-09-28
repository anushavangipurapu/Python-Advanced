# Authentication vs Authorization

## Authentication

Authentication means checking the identity of a user.

It answers:

**"Who are you?"**

### Example

A user enters a username and password.

The system verifies the credentials.

If the credentials are correct, the user is authenticated.

## Authorization

Authorization means checking what an authenticated user is allowed to access or perform.

It answers:

**"What are you allowed to do?"**

### Example

An admin user may have permission to access admin features.

A normal user may not have those permissions.

## Difference

### Authentication

* Checks who the user is.
* Usually happens during login.
* Uses username and password.

### Authorization

* Checks what the user can access or perform.
* Happens after authentication.
* Uses permissions and access rules.

## Simple Example

### Authentication

Username + Password
↓
Verify User
↓
User Authenticated

### Authorization

Authenticated User
↓
Check Permissions
↓
Access Allowed or Denied

## Conclusion

Authentication verifies who the user is.

Authorization determines what the authenticated user is allowed to do.

---

# Django User System

Django provides a built-in User model for managing users.

The main User fields reviewed are:

* `id`
* `username`
* `password`
* `first_name`
* `last_name`
* `email`
* `is_active`
* `is_staff`
* `is_superuser`
* `last_login`
* `date_joined`

Passwords must never be stored as plain text.

Django securely hashes passwords before storing them in the database.

The password field stores a hashed password using Django's password hashing system.

---

# Registration API

## Endpoint

```text
POST /api/v1/auth/register/
```

## Request Fields

```text
username
email
password
password_confirm
first_name
last_name
```

## Registration Features

* Username is required.
* Username must be unique.
* Email is required.
* Email must have a valid format.
* Email must be unique.
* Password is required.
* Password must satisfy Django password validation.
* Password confirmation must match the password.
* Password is stored securely using Django's `create_user()` method.

## Successful Response

```text
User registered successfully.
```

---

# Registration Validation

The following validations were implemented and tested:

* Duplicate username
* Duplicate email
* Invalid email
* Weak password
* Password confirmation mismatch
* Missing required fields

Weak password such as:

```text
123
```

is rejected by the API.

---

# Secure Password Storage

The RegistrationSerializer uses Django's `create_user()` method:

```python
User.objects.create_user(
    username=validated_data["username"],
    email=validated_data["email"],
    password=validated_data["password"],
    first_name=validated_data.get("first_name", ""),
    last_name=validated_data.get("last_name", ""),
)
```

Django hashes the password before storing it.

The password was verified in the database using:

```python
user = User.objects.get(username="anusha_auth")

print(user.password)
print(user.password.startswith("pbkdf2_sha256$"))
```

The password was stored using the `pbkdf2_sha256` hashing mechanism.

Plain-text password is not stored.

---

# Login API

## Endpoint

```text
POST /api/v1/auth/login/
```

## Request

```json
{
    "username": "anusha_auth",
    "password": "StrongPass@123"
}
```

## Login Validation

The login API validates:

* Correct username
* Correct password
* User account status

Django's `authenticate()` method is used for authentication.

Invalid username or password returns an authentication error.

---

# Account Validation

Inactive users must not be allowed to authenticate.

An inactive test user was created:

```text
username: inactive_auth
is_active: False
```

The inactive account was tested with the correct password.

The account was rejected with an authentication error.

The secure authentication implementation using Django's `authenticate()` method was restored after testing.

---

# Debugging Exercise 1 — Incorrect Password Storage

## Issue

Passwords must not be stored as plain text.

## Incorrect Approach

```python
User.objects.create(
    username="test_user",
    password="PlainPassword123"
)
```

This approach must not be used because it can store the password incorrectly.

## Correct Approach

```python
User.objects.create_user(
    username="test_user",
    password="PlainPassword123"
)
```

Django securely hashes the password before storing it.

## Verification

The registered user's password was inspected and confirmed to use the `pbkdf2_sha256` hashing mechanism.

Plain password: Not stored.

Hashed password: Stored.

## Fix

The secure `create_user()` method is used in the `RegistrationSerializer`.

---

# Debugging Exercise 2 — Duplicate Email Accepted

## Issue

Duplicate email registration was temporarily allowed by removing the email uniqueness validation.

## Verification

A second user was registered using an existing email address, and the API incorrectly accepted the registration.

## Fix

The `validate_email()` validation was restored in `RegistrationSerializer`.

## Result

Duplicate email registration is now rejected with a validation error:

```text
Email already exists.
```

The duplicate email validation was tested successfully.

---

# Debugging Exercise 3 — Inactive User Allowed to Login

## Issue

An inactive user must not be allowed to log in.

## Verification

The inactive user `inactive_auth` was tested with the correct password.

## Fix

Authentication was restored using Django's `authenticate()` method and inactive account validation was retained.

## Result

The inactive account was rejected with an authentication error.

---

# Debugging Exercise 4 — Missing Password Validation

## Issue

Password validation was temporarily removed from the registration serializer.

## Verification

The weak password:

```text
123
```

was accepted during the debugging test.

This reproduced the password validation bug.

## Fix

The `validate_password` validator was restored to the password field:

```python
password = serializers.CharField(
    write_only=True,
    validators=[validate_password]
)
```

## Result

The weak password `123` was rejected by the registration API.

The API returned password validation errors including:

```text
This password is too short. It must contain at least 8 characters.
This password is too common.
```

Password validation is working correctly.
