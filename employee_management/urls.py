from django.contrib import admin
from django.urls import include, path

from employees.api.views import MyProfileAPIView

urlpatterns = [
    path("api/v1/reports/", include("reports.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("employees.urls")),
    path("api/v1/", include("employees.api.urls")),

    path(
        "api/v1/profile/me/",
        MyProfileAPIView.as_view(),
        name="my-profile",
    ),

    path("api/v1/auth/", include("accounts.urls")),
]