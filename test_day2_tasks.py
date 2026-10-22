
from django.test import TestCase
from unittest.mock import patch

from employees.models import Department, Employee, Notification
from employees.tasks import send_welcome_email


class WelcomeEmailIdempotencyTests(TestCase):
    def setUp(self):
        self.department = Department.objects.create(
            name="Day2 Test Department",
            code="D2TEST",
        )
        self.employee = Employee.objects.create(
            employee_code="D2-TEST-001",
            first_name="Test",
            last_name="Employee",
            email="day2.test@example.com",
            phone="9999999999",
            department=self.department,
            designation="Tester",
            salary="30000.00",
            joining_date="2026-10-22",
        )

    @patch("employees.tasks.EmailMultiAlternatives")
    @patch("employees.tasks.render_to_string", return_value="<p>Welcome</p>")
    def test_duplicate_execution_sends_email_only_once(
        self, mock_template, mock_email_class
    ):
        mock_email = mock_email_class.return_value
        mock_email.send.return_value = 1

        first_result = send_welcome_email.run(self.employee.pk)
        second_result = send_welcome_email.run(self.employee.pk)

        self.assertIn("sent", first_result.lower())
        self.assertIn("already sent", second_result.lower())
        self.assertEqual(mock_email.send.call_count, 1)

        notification = Notification.objects.get(
            employee=self.employee,
            notification_type="WELCOME",
        )
        self.assertTrue(notification.email_sent)

    def test_missing_employee_fails(self):
        with self.assertRaises(Employee.DoesNotExist):
            send_welcome_email.run(999999)
