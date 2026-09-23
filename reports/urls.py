from django.urls import path
from .views import department_summary, project_summary, salary_summary

urlpatterns = [
    path("department-summary/", department_summary, name="department-summary"),
    path("project-summary/", project_summary, name="project-summary"),
    path("salary-summary/", salary_summary, name="salary-summary"),
]
