
from django.urls import path

from .health import health_check
from .views import (
    EmployeeViewSet,
    MyProfileAPIView,
    EmployeeProfileAPIView,
    NotificationListAPIView,
    NotificationMarkReadAPIView,
    DepartmentEmployeeStatsAPIView,
)


employee_list = EmployeeViewSet.as_view({
    "get": "list",
    "post": "create",
})

employee_detail = EmployeeViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

employee_active = EmployeeViewSet.as_view({
    "get": "active",
})


urlpatterns = [
    path(
        "health/",
        health_check,
        name="health",
    ),

    path(
        "employees/",
        employee_list,
        name="employee-list",
    ),

    path(
        "employees/active/",
        employee_active,
        name="employee-active",
    ),

    path(
        "employees/<int:pk>/",
        employee_detail,
        name="employee-detail",
    ),

    path(
        "profile/me/",
        MyProfileAPIView.as_view(),
        name="my-profile",
    ),

    path(
        "employees/<int:pk>/profile/",
        EmployeeProfileAPIView.as_view(),
        name="employee-profile",
    ),

    path(
        "notifications/",
        NotificationListAPIView.as_view(),
        name="notification-list",
    ),

    path(
        "notifications/<int:pk>/read/",
        NotificationMarkReadAPIView.as_view(),
        name="notification-mark-read",
    ),

    path(
        "departments/stats/",
        DepartmentEmployeeStatsAPIView.as_view(),
        name="department-stats",
    ),
]
