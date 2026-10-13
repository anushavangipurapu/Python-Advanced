
from datetime import date
from decimal import Decimal

from django.core.cache import cache
from django.test import TestCase

from employees.cache_services import (
    DEPARTMENT_STATS_CACHE_KEY,
    get_department_employee_stats,
    invalidate_department_employee_stats,
)
from employees.models import Department, Employee


class DepartmentStatsCacheTests(TestCase):
    def setUp(self):
        cache.delete(DEPARTMENT_STATS_CACHE_KEY)

        self.department = Department.objects.create(
            name="Cache Test Department",
            code="CACHE-TEST",
        )

    def tearDown(self):
        cache.delete(DEPARTMENT_STATS_CACHE_KEY)

    def test_employee_creation_invalidates_department_stats(self):
        # Step 1: Cache the statistics before employee creation.
        initial_stats = get_department_employee_stats()

        department_stats = next(
            item for item in initial_stats
            if item["id"] == self.department.id
        )
        self.assertEqual(department_stats["total_employees"], 0)
        self.assertIsNotNone(cache.get(DEPARTMENT_STATS_CACHE_KEY))

        # Step 2: Create an employee.
        Employee.objects.create(
            employee_code="CACHE-EMP-001",
            first_name="Cache",
            last_name="Tester",
            email="cache.tester@example.com",
            phone="9000000001",
            department=self.department,
            designation="Developer",
            salary=Decimal("30000.00"),
            joining_date=date(2026, 1, 1),
            is_active=True,
        )

        # Step 3: Simulate the invalidation performed after an employee write.
        invalidate_department_employee_stats()

        self.assertIsNone(cache.get(DEPARTMENT_STATS_CACHE_KEY))

        # Step 4: Fetch fresh statistics.
        refreshed_stats = get_department_employee_stats()

        refreshed_department_stats = next(
            item for item in refreshed_stats
            if item["id"] == self.department.id
        )
        self.assertEqual(
            refreshed_department_stats["total_employees"],
            1,
        )
        self.assertEqual(
            refreshed_department_stats["active_employees"],
            1,
        )
from unittest.mock import patch

from rest_framework.test import APITestCase
from django.urls import reverse


class EmployeeAPICacheInvalidationTests(APITestCase):
    @patch("employees.api.views.invalidate_department_employee_stats")
    def test_employee_create_calls_cache_invalidation(self, mock_invalidate):
        # This test verifies that the create API calls cache invalidation.
        # Authentication/authorization is bypassed here so the test
        # focuses specifically on the view's cache invalidation hook.
        from rest_framework.test import APIRequestFactory, force_authenticate
        from django.contrib.auth.models import User
        from employees.api.views import EmployeeViewSet

        user = User.objects.create_user(
            username="cache_admin_test",
            password="TestPassword123!",
        )

        # Attach an ADMIN profile using the Employee model.
        from employees.models import Department, Employee

        department = Department.objects.create(
            name="API Cache Test Department",
            code="API-CACHE-TEST",
        )

        admin_employee = Employee.objects.create(
            user=user,
            role="ADMIN",
            employee_code="EMP99001",
            first_name="Cache",
            last_name="Admin",
            email="cache.admin@example.com",
            phone="9000000099",
            department=department,
            designation="Administrator",
            salary="50000.00",
            joining_date="2025-01-01",
        )

        factory = APIRequestFactory()
        request = factory.post(
            "/api/v1/employees/",
            {
                "employee_code": "EMP99002",
                "first_name": "New",
                "last_name": "Employee",
                "email": "new.cache.employee@example.com",
                "phone": "9000000098",
                "department": department.id,
                "designation": "Developer",
                "salary": "30000.00",
                "joining_date": "2025-02-01",
                "is_active": True,
            },
            format="json",
        )
        force_authenticate(request, user=user)

        view = EmployeeViewSet.as_view({"post": "create"})
        response = view(request)

        self.assertEqual(response.status_code, 201)
        mock_invalidate.assert_called_once()
