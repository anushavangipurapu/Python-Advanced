from django.urls import path

from .views import (
    health_check,
    employee_list,
    employee_detail,
    employee_details,
    invalid_redirect,
)


urlpatterns = [
    path("health/", health_check, name="health"),
    path("employees/", employee_list, name="employee-list"),
    path("employees/<int:id>/", employee_detail, name="employee-detail"),
    path("employees/details/", employee_details, name="employee-details"),

    # Debugging Exercise - Broken URL
    path("invalid-redirect/", invalid_redirect, name="invalid-redirect-broken"),
]