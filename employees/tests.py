
from datetime import date
from decimal import Decimal
from unittest.mock import patch

from django.core.cache import cache
from django.test import TestCase
from rest_framework.test import APITestCase

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
        initial_stats = get_department_employee_stats()

        department_stats = next(
            item for item in initial_stats
            if item["id"] == self.department.id
        )

        self.assertEqual(department_stats["total_employees"], 0)
        self.assertIsNotNone(cache.get(DEPARTMENT_STATS_CACHE_KEY))

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

        invalidate_department_employee_stats()

        self.assertIsNone(cache.get(DEPARTMENT_STATS_CACHE_KEY))

        refreshed_stats = get_department_employee_stats()

        refreshed_department_stats = next(
            item for item in refreshed_stats
            if item["id"] == self.department.id
        )

        self.assertEqual(
            refreshed_department_stats["total_employees"], 1
        )
        self.assertEqual(
            refreshed_department_stats["active_employees"], 1
        )


class EmployeeAPICacheInvalidationTests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(
            name="API Cache Test Department",
            code="API-CACHE",
        )

    def test_employee_creation_invalidates_department_stats(self):
        initial_stats = get_department_employee_stats()

        self.assertTrue(
            any(
                item["id"] == self.department.id
                for item in initial_stats
            )
        )

        self.assertIsNotNone(cache.get(DEPARTMENT_STATS_CACHE_KEY))

        Employee.objects.create(
            employee_code="API-CACHE-001",
            first_name="API",
            last_name="Tester",
            email="api.cache@example.com",
            phone="9000000002",
            department=self.department,
            designation="Developer",
            salary=Decimal("30000.00"),
            joining_date=date(2026, 1, 1),
            is_active=True,
        )

        invalidate_department_employee_stats()

        self.assertIsNone(cache.get(DEPARTMENT_STATS_CACHE_KEY))


class DepartmentStatsCacheFailureTests(TestCase):
    def setUp(self):
        cache.delete(DEPARTMENT_STATS_CACHE_KEY)

        self.department = Department.objects.create(
            name="Cache Failure Test Department",
            code="CACHE-FAIL",
        )

    def tearDown(self):
        cache.delete(DEPARTMENT_STATS_CACHE_KEY)

    @patch(
        "employees.cache_services.cache.get",
        side_effect=Exception("Simulated cache read failure"),
    )
    def test_cache_read_failure_falls_back_to_database(
        self, mock_get
    ):
        stats = get_department_employee_stats()

        self.assertTrue(
            any(
                item["id"] == self.department.id
                for item in stats
            )
        )

        mock_get.assert_called_once()

    @patch("employees.cache_services.get_redis_connection")
    @patch(
        "employees.cache_services.cache.get",
        return_value=None,
    )
    @patch("employees.cache_services.cache.set")
    def test_cache_write_failure_still_returns_database_results(
        self, mock_set, mock_get, mock_redis_connection
    ):
        mock_lock = mock_redis_connection.return_value.lock.return_value
        mock_lock.acquire.return_value = True

        mock_set.side_effect = Exception(
            "Simulated cache write failure"
        )

        stats = get_department_employee_stats()

        self.assertTrue(
            any(
                item["id"] == self.department.id
                for item in stats
            )
        )

        self.assertEqual(mock_get.call_count, 2)
        mock_set.assert_called_once()
        mock_lock.release.assert_called_once()

    @patch(
        "employees.cache_services.cache.delete",
        side_effect=Exception("Simulated cache delete failure"),
    )
    def test_cache_invalidation_failure_does_not_crash(
        self, mock_delete
    ):
        invalidate_department_employee_stats()

        mock_delete.assert_called_once()
