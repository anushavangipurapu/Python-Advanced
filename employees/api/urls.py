from django.urls import path

from .views import (
    EmployeeViewSet,
    MyProfileAPIView,
    EmployeeProfileAPIView,
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


urlpatterns = [
    path(
        "employees/",
        employee_list,
        name="employee-list",
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
]