# OWASP API Security Review

## 1. Broken Object Level Authorization (BOLA)

### Risk
An authenticated user may access another user's or employee's object by changing the object ID.

### Control
Object-level authorization must be checked before returning or modifying employee data.

### Review
Employee detail and update/delete operations should verify that the authenticated user has permission to access the requested employee object.

---

## 2. Broken Authentication

### Risk
Weak authentication or missing authentication can allow unauthorized users to access protected APIs.

### Control
Protected API endpoints require authentication.

JWT authentication is used for API authentication.

### Review
Authentication configuration and protected endpoints should be reviewed to ensure unauthenticated users cannot access protected resources.

---

## 3. Broken Object Property Level Authorization (BOPLA)

### Risk
Users may modify or access properties that they are not authorized to change.

### Control
Serializers and permissions should restrict sensitive fields and prevent unauthorized field modification.

### Review
Sensitive employee properties should not be exposed or modified unless the authenticated user has the required permission.

---

## 4. Unrestricted Resource Consumption

### Risk
Repeated or excessive API requests can consume server resources.

### Control
DRF throttling is configured.

Configured rates:

- Anonymous users: 10 requests per minute
- Authenticated users: 60 requests per minute

Repeated-request testing will be performed during the final security testing phase.

---

## 5. Security Misconfiguration

### Risk
Incorrect security settings can expose the application to attacks.

### Control

The following areas were reviewed:

- DEBUG
- SECRET_KEY
- ALLOWED_HOSTS
- CORS
- CSRF
- Secure cookies
- HTTPS configuration
- Environment variables

CORS is configured using specific allowed origins instead of allowing all origins.

Secrets are stored outside source code using environment variables.

---

## 6. Improper Inventory Management

### Risk
Old, unused, undocumented, or unprotected API endpoints may increase the attack surface.

### Control
API routes should be reviewed and documented.

Unused or legacy endpoints should be identified and removed or protected when appropriate.

### Review
The project API endpoints should be reviewed to ensure that only required endpoints are exposed.

---

# Security Review Conclusion

The API was reviewed against the selected OWASP API Security risks.

The review covers:

- Object-level authorization
- Authentication
- Property-level authorization
- Resource consumption
- Security configuration
- API inventory

Remaining security testing, including repeated-request/rate-limit testing, will be completed during the final testing phase.