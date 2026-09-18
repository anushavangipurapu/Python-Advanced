from rest_framework.test import APITestCase

from employees.models import Employee


class EmployeeAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(
            employee_code="EMP001",
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
            employee_code="EMP002",
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
            employee_code="EMP003",
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
        response = self.client.get(
            "/api/v1/employees/"
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_active_employees(self):
        response = self.client.get(
            "/api/v1/employees/active/"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        for employee in response.data:
            self.assertTrue(
                employee["is_active"]
            )

    def test_department_filter(self):
        response = self.client.get(
            "/api/v1/employees/?department=Backend"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        for employee in response.data["results"]:
            self.assertEqual(
                employee["department"],
                "Backend"
            )

    def test_search_employee(self):
        response = self.client.get(
            "/api/v1/employees/?search=Divya"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTrue(
            any(
                employee["first_name"] == "Divya"
                for employee in response.data["results"]
            )
        )

    def test_salary_ordering_descending(self):
        response = self.client.get(
            "/api/v1/employees/?ordering=-salary"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        salaries = [
            float(employee["salary"])
            for employee in response.data["results"]
        ]

        self.assertEqual(
            salaries,
            sorted(salaries, reverse=True)
        )

    def test_combined_filters(self):
        response = self.client.get(
            "/api/v1/employees/"
            "?department=Backend&is_active=true&ordering=-salary"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        for employee in response.data["results"]:
            self.assertEqual(
                employee["department"],
                "Backend"
            )

            self.assertTrue(
                employee["is_active"]
            )

        salaries = [
            float(employee["salary"])
            for employee in response.data["results"]
        ]

        self.assertEqual(
            salaries,
            sorted(salaries, reverse=True)
        )

    def test_pagination(self):
        response = self.client.get(
            "/api/v1/employees/?page=1"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIn(
            "count",
            response.data
        )

        self.assertIn(
            "next",
            response.data
        )

        self.assertIn(
            "previous",
            response.data
        )

        self.assertIn(
            "results",
            response.data
        )

    def test_create_employee(self):
        data = {
            "employee_code": "EMP004",
            "first_name": "Anusha",
            "last_name": "V",
            "email": "anusha_test@example.com",
            "phone": "9876543213",
            "department": "Backend",
            "designation": "Developer",
            "salary": 70000,
            "joining_date": "2025-03-15",
            "is_active": True,
        }

        response = self.client.post(
            "/api/v1/employees/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            201
        )

    def test_retrieve_employee(self):
        employee = Employee.objects.get(
            employee_code="EMP001"
        )

        response = self.client.get(
            f"/api/v1/employees/{employee.id}/"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            response.data["employee_code"],
            "EMP001"
        )

    def test_update_employee(self):
        employee = Employee.objects.get(
            employee_code="EMP001"
        )

        data = {
            "employee_code": "EMP001",
            "first_name": "Ravi",
            "last_name": "Updated",
            "email": "ravi_test@example.com",
            "phone": "9876543210",
            "department": "Backend",
            "designation": "Senior Developer",
            "salary": 90000,
            "joining_date": "2025-01-15",
            "is_active": True,
        }

        response = self.client.put(
            f"/api/v1/employees/{employee.id}/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_partial_update_employee(self):
        employee = Employee.objects.get(
            employee_code="EMP002"
        )

        response = self.client.patch(
            f"/api/v1/employees/{employee.id}/",
            {
                "salary": 65000
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_delete_employee(self):
        employee = Employee.objects.create(
            employee_code="EMP005",
            first_name="Delete",
            last_name="Test",
            email="delete_test@example.com",
            phone="9876543214",
            department="IT",
            designation="Tester",
            salary=50000,
            joining_date="2025-04-15",
            is_active=True,
        )

        response = self.client.delete(
            f"/api/v1/employees/{employee.id}/"
        )

        self.assertEqual(
            response.status_code,
            204
        )

    def test_duplicate_email_validation(self):
        data = {
            "employee_code": "EMP006",
            "first_name": "Duplicate",
            "last_name": "Email",
            "email": "ravi_test@example.com",
            "phone": "9876543215",
            "department": "IT",
            "designation": "Developer",
            "salary": 50000,
            "joining_date": "2025-05-15",
            "is_active": True,
        }

        response = self.client.post(
            "/api/v1/employees/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            400
        )

    def test_negative_salary_validation(self):
        data = {
            "employee_code": "EMP007",
            "first_name": "Invalid",
            "last_name": "Salary",
            "email": "invalid_salary@example.com",
            "phone": "9876543216",
            "department": "IT",
            "designation": "Developer",
            "salary": -5000,
            "joining_date": "2025-05-15",
            "is_active": True,
        }

        response = self.client.post(
            "/api/v1/employees/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            400
        )

    def test_invalid_employee_404(self):
        response = self.client.get(
            "/api/v1/employees/9999/"
        )

        self.assertEqual(
            response.status_code,
            404
        )

        self.assertEqual(
            response.data["detail"],
            "Employee not found."
        )