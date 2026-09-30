from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "employee_profile")
            and request.user.employee_profile.role == "ADMIN"
        )


class IsHR(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "employee_profile")
            and request.user.employee_profile.role == "HR"
        )


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "employee_profile")
            and request.user.employee_profile.role == "MANAGER"
        )


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "employee_profile")
            and request.user.employee_profile.role == "EMPLOYEE"
        )