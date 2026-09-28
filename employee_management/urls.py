from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/v1/reports/", include("reports.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("employees.urls")),
    path("api/v1/", include("employees.api.routers")),
    path("api/v1/auth/", include("accounts.urls")),
]
