# SEC-005 — Security Audit, Penetration-Style Testing & Code Review

**Date:** 02-Oct-2026  
**Project:** Employee Management Backend  
**Framework:** Django + Django REST Framework  
**Status:** Completed

---

## 1. Security Audit Summary

A security audit and penetration-style testing review was performed on the Employee Management Backend.

The audit covered:

- Authentication
- JWT authentication
- Authorization
- Role-based access control
- Object-level authorization
- API input validation
- Authentication abuse testing
- Error handling
- Security configuration
- Sensitive data protection
- Security-related code review

---

# 2. Authentication Audit

## 2.1 Registration

**Endpoint:**

`POST /api/v1/auth/register/`

**Result:** PASS

A new security test user was successfully registered.

---

## 2.2 JWT Token Generation

**Endpoint:**

`POST /api/v1/auth/token/`

**Result:** PASS

Valid credentials successfully generated:

- Access token
- Refresh token

---

## 2.3 JWT Refresh

**Endpoint:**

`POST /api/v1/auth/token/refresh/`

**Result:** PASS

A valid refresh token successfully generated a new access token.

---

## 2.4 Invalid JWT

**Endpoint:**

`GET /api/v1/profile/me/`

**Result:** PASS

An invalid JWT token was rejected and authentication failed.

---

## 2.5 Expired JWT

**Result:** PASS

An expired access token was rejected with an authentication error.

---

## 2.6 Inactive Account

**Result:** PASS

An inactive user account was not allowed to obtain a JWT token.

---

## 2.7 Missing Authorization Header

**Result:** PASS

Requests without an Authorization header were rejected.

---

# 3. Authorization Audit

The following roles were tested:

- ADMIN
- HR
- MANAGER
- EMPLOYEE

## Results

| Role | Employee API Access | Result |
|------|---------------------|--------|
| ADMIN | Full access | PASS |
| HR | Employee management access | PASS |
| MANAGER | Restricted employee access | PASS |
| EMPLOYEE | Own employee access | PASS |

Employee users were restricted to their own employee record where object-level authorization was required.

---

# 4. Object-Level Authorization Testing

## 4.1 Employee Accessing Own Profile

**Endpoint:**

`GET /api/v1/profile/me/`

**Result:** PASS

Authenticated employee successfully accessed their own profile.

---

## 4.2 Employee Accessing Another Employee Profile

**Endpoint:**

`GET /api/v1/employees/<id>/profile/`

**Result:** PASS

Employee access to another employee profile was rejected with HTTP 403.

---

## 4.3 Manager Accessing Another Employee Profile

A manager was tested against another employee profile.

An authorization issue was identified during testing and the profile authorization logic was updated.

The manager is now restricted from accessing another employee profile.

**Result:** FIXED

---

## 4.4 HR Profile Access

HR users are allowed to manage employee profiles according to the defined role permissions.

**Result:** PASS

---

## 4.5 Admin Profile Access

Admin users have full employee profile access according to the defined role permissions.

**Result:** PASS

---

# 5. API Input Security Testing

The API was tested with invalid and unexpected input.

## 5.1 Missing Required Fields

**Result:** PASS

Required-field validation rejected incomplete requests.

---

## 5.2 Invalid Data Types

**Result:** PASS

Invalid data types and invalid values were rejected by serializer validation.

---

## 5.3 Large Values

**Result:** PASS

Large salary values were rejected when they exceeded the configured validation limits.

---

## 5.4 Unexpected Fields

**Result:** FINDING

An unexpected field was accepted/ignored by the serializer during testing.

**Severity:** Medium

**Issue:**

The API did not explicitly reject an unexpected field.

**Recommendation:**

Review serializer field handling and explicitly reject unexpected input where strict request validation is required.

---

## 5.5 Invalid Employee ID

**Result:** PASS

Invalid employee IDs returned an appropriate not-found response.

---

## 5.6 Malformed JSON

**Result:** PASS

Malformed JSON was rejected with a JSON parsing error.

---

## 5.7 Invalid Query Parameter

**Result:** PASS

Invalid pagination/query parameter values were handled safely.

---

# 6. Authentication Abuse Testing

## 6.1 Invalid Credentials

**Result:** PASS

Invalid login credentials were rejected with HTTP 401.

---

## 6.2 Repeated Login Attempts

Ten repeated invalid login attempts were performed.

**Observed result:**

All attempts returned HTTP 401.

No HTTP 429 response was observed during this specific ten-attempt test.

**Result:** FINDING / REVIEW REQUIRED

The login endpoint should be reviewed to ensure authentication abuse protection and rate limiting are applied as intended.

---

## 6.3 Invalid Refresh Token

**Result:** PASS

Invalid refresh tokens were rejected.

---

## 6.4 Modified JWT

**Result:** PASS

A modified JWT token was rejected.

---

## 6.5 Expired Access Token

**Result:** PASS

Expired access tokens were rejected.

---

# 7. Error Handling Audit

## 7.1 Invalid Endpoint

Invalid endpoints were tested.

A development 404 response exposed internal URL configuration information because Django DEBUG mode was enabled.

**Result:** FINDING

---

# 8. Security Findings

## Finding ID: SEC-005-F001

**Severity:** Medium

**Affected Endpoint:** Invalid/non-existing endpoints

**Issue:**

Django DEBUG mode was enabled.

Development error responses exposed internal URL pattern information.

**Steps to Reproduce:**

1. Request an invalid API endpoint.
2. Observe the Django 404 response.
3. Internal URL patterns and route information are visible.

**Expected Behavior:**

Production responses should not expose internal application configuration or URL patterns.

**Actual Behavior:**

Debug information was exposed in the response.

**Root Cause:**

`DEBUG=True` in Django settings.

**Fix:**

Set `DEBUG=False` in production and configure appropriate production error handling.

**Regression Test:**

Request an invalid endpoint with production configuration and verify that internal debug information is not exposed.

**Status:**

Open / Production Configuration Required

---

## Finding ID: SEC-005-F002

**Severity:** High

**Affected Component:** Django settings

**Issue:**

The Django SECRET_KEY was configured directly in the settings file.

**Steps to Reproduce:**

1. Review `settings.py`.
2. Inspect the SECRET_KEY configuration.

**Expected Behavior:**

Secrets should be stored outside source code using environment variables or secure secret management.

**Actual Behavior:**

The secret key was present in application configuration.

**Root Cause:**

Hardcoded secret configuration.

**Fix:**

Move SECRET_KEY to environment-based configuration and rotate the exposed development secret.

**Regression Test:**

Verify that the application loads SECRET_KEY from environment configuration and that no secret is committed to source control.

**Status:**

Open / Security Hardening Required

---

## Finding ID: SEC-005-F003

**Severity:** High

**Affected Endpoint:**

`GET /api/v1/employees/<id>/profile/`

**Issue:**

A manager was able to access another employee profile during the initial object-level authorization test.

**Steps to Reproduce:**

1. Authenticate as a manager.
2. Request another employee's profile.
3. Observe that the profile was initially returned.

**Expected Behavior:**

Managers should not access another employee profile when the defined ownership rule restricts access.

**Actual Behavior:**

The profile was initially accessible.

**Root Cause:**

Missing manager ownership validation in the profile API.

**Fix:**

Added manager ownership validation to the profile endpoint.

**Regression Test:**

Manager access to another employee profile must return HTTP 403.

**Status:**

Fixed

---

## Finding ID: SEC-005-F004

**Severity:** Medium

**Affected Component:** Employee serializer

**Issue:**

Unexpected fields were not explicitly rejected during input validation.

**Steps to Reproduce:**

1. Send an employee creation request.
2. Add an unexpected field.
3. Observe that the request was accepted/processed.

**Expected Behavior:**

Unexpected request fields should be rejected when strict input validation is required.

**Actual Behavior:**

The unexpected field was ignored/accepted.

**Root Cause:**

Serializer field handling.

**Fix:**

Review serializer validation and enforce strict input handling where required.

**Regression Test:**

Submit a request containing an unexpected field and verify the expected validation response.

**Status:**

Review Required

---

## Finding ID: SEC-005-F005

**Severity:** Medium

**Affected Endpoint:**

`POST /api/v1/auth/token/`

**Issue:**

No HTTP 429 response was observed during ten repeated invalid login attempts.

**Steps to Reproduce:**

1. Send repeated login requests with invalid credentials.
2. Perform ten attempts.
3. Observe the HTTP responses.

**Expected Behavior:**

Authentication abuse controls should limit repeated failed authentication attempts according to the security configuration.

**Actual Behavior:**

All ten tested attempts returned HTTP 401.

**Root Cause:**

Rate-limit behavior for the login endpoint requires further verification.

**Fix:**

Review authentication throttling configuration and ensure login abuse protection is applied as intended.

**Regression Test:**

Repeat failed authentication attempts and verify that the configured throttle behavior is triggered.

**Status:**

Review Required

---

# 9. Security Configuration Review

The following areas were reviewed:

- DEBUG configuration
- SECRET_KEY configuration
- ALLOWED_HOSTS
- CORS configuration
- CSRF middleware
- JWT configuration
- DRF throttling
- Authentication configuration
- Permission configuration

## JWT Configuration

Access token lifetime:

`5 minutes`

Refresh token lifetime:

`1 day`

## CORS

Configured CORS origins were reviewed.

No wildcard CORS origin was identified during the review.

## CSRF

Django CSRF middleware was present.

## DRF Throttling

DRF anonymous and user throttling configuration was reviewed.

---

# 10. Final Practical Security Tests

| Test | Expected Result | Status |
|------|------------------|--------|
| Anonymous profile access | 401 | PASS |
| Authenticated employee own profile | 200 | PASS |
| Employee accessing another profile | 403 | PASS |
| HR accessing employee profile | 200 | PASS |
| Admin accessing employee profile | 200 | PASS |
| Invalid JWT | 401 | PASS |
| Expired JWT | 401 | PASS |
| Invalid input | 400 | PASS |
| Missing required fields | 400 | PASS |
| Unauthorized profile update | 403 | PASS |

---

# 11. Code Review

The following components were reviewed:

- `models.py`
- `serializers.py`
- `views.py`
- `permissions.py`
- Authentication implementation
- `settings.py`
- `urls.py`

The review focused on:

- Authentication
- Authorization
- Object ownership
- Input validation
- Error handling
- Sensitive data protection
- Security configuration
- Code readability
- Maintainability

The profile API authorization logic was updated during the audit to enforce role and ownership restrictions.

---

# 12. Overall Audit Result

The Employee Management Backend completed authentication, authorization, object-level authorization, input validation, authentication abuse testing, error handling review, and security configuration review.

Security issues identified during the audit were documented with reproduction steps, root causes, fixes, and regression test requirements.

The remaining security findings are primarily related to production configuration and additional hardening.

**SEC-005 Security Audit: Completed**

**Final Status:** Audit Completed