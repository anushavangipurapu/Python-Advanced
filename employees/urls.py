from django.urls import path
from .views import health_check, employee_list, employee_detail


urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("employees/", employee_list, name="employee-list"),
   path("employees/<int:id>/", employee_detail, name="employee-detail"),
]