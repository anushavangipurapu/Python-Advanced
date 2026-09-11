from django.urls import path

from .views import (
    health_check,
    employee_list,
    employee_detail,
    invalid_redirect,
)


urlpatterns = [
    path("health/", health_check, name="health"),
    path("employees/", employee_list, name="employee-list"),
    path("employees/<int:id>/", employee_detail, name="employee-detail"),

    # Debugging Exercise - Invalid Redirect
    path("invalid-redirect/", invalid_redirect, name="invalid-redirect"),
]