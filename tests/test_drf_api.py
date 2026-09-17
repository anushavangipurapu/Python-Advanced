from django.urls import reverse
from rest_framework.test import APITestCase

from employees.models import Employee


class EmployeeAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(
            employee_code="TEST001",
            first_name="Ravi",
            last_name="Kumar",
            email="ravi_test@example.com",
            phone="9876543210",
            department="Backend",
            designation="Python Developer",
            salary=85000,
            joining_date="2025-01-15",
            is_active=True,
        )

        Employee.objects.create(
            employee_code="TEST002",
            first_name="Divya",
            last_name="Reddy",
            email="divya_test@example.com",
            phone="9876543211",
            department="IT",
            designation="Developer",
            salary=60000,
            joining_date="2025-02-15",
            is_active=True,
        )

        Employee.objects.create(
            employee_code="TEST003",
            first_name="Anu",
            last_name="Devi",
            email="anu_test@example.com",
            phone="9876543212",
            department="Backend",
            designation="Senior Developer",
            salary=95000,
            joining_date="2024-12-15",
            is_active=False,
        )

    def test_list_employees(self):
        response = self.client.get("/api/v1/employees/")

        self.assertEqual(response.status_code, 200)

    def test_active_employees(self):
        response = self.client.get("/api/v1/employees/active/")

        self.assertEqual(response.status_code, 200)

        for employee in response.data:
            self.assertTrue(employee["is_active"])

    def test_department_filter(self):
        response = self.client.get(
            "/api/v1/employees/?department=Backend"
        )

        self.assertEqual(response.status_code, 200)

        for employee in response.data:
            self.assertEqual(employee["department"], "Backend")

    def test_search_employee(self):
        response = self.client.get(
            "/api/v1/employees/?search=Divya"
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            any(
                employee["first_name"] == "Divya"
                for employee in response.data
            )
        )

    def test_salary_ordering_descending(self):
        response = self.client.get(
            "/api/v1/employees/?ordering=-salary"
        )

        self.assertEqual(response.status_code, 200)

        salaries = [
            float(employee["salary"])
            for employee in response.data
        ]

        self.assertEqual(salaries, sorted(salaries, reverse=True))

    def test_combined_filters(self):
        response = self.client.get(
            "/api/v1/employees/"
            "?department=Backend&is_active=true&ordering=-salary"
        )

        self.assertEqual(response.status_code, 200)

        for employee in response.data:
            self.assertEqual(employee["department"], "Backend")
            self.assertTrue(employee["is_active"])

        salaries = [
            float(employee["salary"])
            for employee in response.data
        ]

        self.assertEqual(salaries, sorted(salaries, reverse=True))