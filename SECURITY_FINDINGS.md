# SEC-004 — Security Findings

## Finding 1 — CSRF Exempt API Views

### Observation
The following function-based API views use `@csrf_exempt`:

- `employee_list`
- `employee_detail`

### Risk
CSRF protection is bypassed for these views.

### Assessment
The project currently uses JWT authentication for API authentication. The use of `csrf_exempt` should still be reviewed if browser-based cookie authentication is introduced.

### Action
Keep CSRF middleware enabled and review `csrf_exempt` usage according to the authentication mechanism.

### Status
Reviewed.

---

## Finding 2 — CORS Configuration

### Observation
CORS is configured with a specific allowed origin:

`http://localhost:3000`

`CORS_ALLOW_ALL_ORIGINS` is not enabled.

### Risk
Overly permissive CORS configuration can allow unauthorized websites to make cross-origin requests.

### Action
Use only trusted frontend origins in production.

### Status
Resolved / Controlled.

---

## Finding 3 — Secrets and Environment Configuration

### Observation
Application secrets and database configuration are managed through environment configuration.

`.env.example` contains placeholder values and `.env` is excluded through `.gitignore`.

### Risk
Committing real secrets to source control could expose credentials.

### Action
Keep real secrets outside source control and use environment variables.

### Status
Resolved / Controlled.

---

## Finding 4 — Rate Limiting

### Observation
DRF throttling is configured with:

- Anonymous users: `10/min`
- Authenticated users: `60/min`

Login and registration endpoints use `AnonRateThrottle`.

### Risk
Without rate limiting, repeated requests could increase resource consumption or facilitate automated authentication attempts.

### Action
Keep throttling enabled and perform repeated-request testing during final security testing.

### Status
Configured — Testing Pending.

---

## Finding 5 — Sensitive Data Exposure Review

### Observation
API responses were reviewed for passwords, password hashes, JWT/private tokens, database credentials, and internal secrets.

### Result
These sensitive authentication and infrastructure secrets are not intentionally returned by the reviewed API responses.

### Action
Continue reviewing serializers and API responses whenever new fields are added.

### Status
Reviewed.

---

## Finding 6 — Input Validation

### Observation
Input validation was reviewed for:

- Empty values
- Invalid data types
- Very large values
- Unexpected fields
- Invalid IDs
- Invalid dates
- Negative salary
- Malformed email

### Action
Validation should continue to be enforced at serializer/API boundaries.

### Status
Reviewed.

---

## Finding 7 — SQL Injection Awareness

### Observation
Django ORM queries use parameterized database operations.

Unsafe string-concatenated SQL was reviewed conceptually, and parameterized raw SQL was reviewed as the safe alternative.

### Action
Avoid constructing SQL queries by directly concatenating user input.

### Status
Reviewed.

---

## Finding 8 — OWASP API Security Review

The API was reviewed against the following OWASP API security areas:

- Broken Object Level Authorization (BOLA)
- Broken Authentication
- Broken Object Property Level Authorization (BOPLA)
- Unrestricted Resource Consumption
- Security Misconfiguration
- Improper Inventory Management

### Status
Reviewed.

---

# Final Findings Summary

| Finding | Status |
|---|---|
| CSRF Exempt Views | Reviewed |
| CORS Configuration | Controlled |
| Secret Management | Controlled |
| Rate Limiting | Configured — Testing Pending |
| Sensitive Data Exposure | Reviewed |
| Input Validation | Reviewed |
| SQL Injection Awareness | Reviewed |
| OWASP API Security | Reviewed |

## Remaining Work

Final security testing remains pending, including:

- Authentication testing
- Authorization testing
- Input validation testing
- Rate limiting testing
- CORS testing
- Sensitive data exposure testing
- Security configuration verification