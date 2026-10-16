
from datetime import date
from decimal import Decimal
from unittest.mock import patch

from django.test import TestCase

from employees.models import Department, Employee, Notification
from employees.tasks import send_welcome_email


class WelcomeEmailIdempotencyTest(TestCase):
    @patch("employees.tasks.EmailMultiAlternatives.send")
    def test_duplicate_execution_does_not_send_email_twice(self, mock_send):
        department = Department.objects.create(
            name="Idempotency Test Department",
            code="IDEMP-TEST",
        )

        employee = Employee.objects.create(
            employee_code="IDEMP-TEST-001",
            first_name="Retry",
            last_name="Test",
            email="retry-test@example.com",
            phone="9000000001",
            department=department,
            designation="Test Engineer",
            salary=Decimal("30000.00"),
            joining_date=date(2026, 1, 1),
        )

        first_result = send_welcome_email.run(employee.pk)
        second_result = send_welcome_email.run(employee.pk)

        self.assertIn("Welcome email sent", first_result)
        self.assertIn("already sent", second_result)
        self.assertEqual(mock_send.call_count, 1)

        notification_count = Notification.objects.filter(
            employee=employee,
            notification_type="WELCOME",
        ).count()

        self.assertEqual(notification_count, 1)
