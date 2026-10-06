from datetime import date

from django.core.management.base import BaseCommand

from employees.models import Employee, Department


class Command(BaseCommand):
    help = "Seed sample employee records"

    def handle(self, *args, **options):
        department = Department.objects.filter(is_active=True).first()

        if not department:
            self.stdout.write(
                self.style.ERROR("No active department found.")
            )
            return

        employees = [
            {
                "employee_code": "EMP001",
                "first_name": "Anusha",
                "last_name": "V",
                "email": "anusha@example.com",
                "phone": "9876543210",
                "designation": "Python Developer",
                "salary": 60000,
                "joining_date": date(2026, 1, 10),
                "role": "EMPLOYEE",
                "is_active": True,
            },
            {
                "employee_code": "EMP002",
                "first_name": "Rahul",
                "last_name": "K",
                "email": "rahul@example.com",
                "phone": "9876543211",
                "designation": "Django Developer",
                "salary": 65000,
                "joining_date": date(2026, 2, 15),
                "role": "EMPLOYEE",
                "is_active": True,
            },
        ]

        created_count = 0
        skipped_count = 0

        for data in employees:
            employee, created = Employee.objects.get_or_create(
                employee_code=data["employee_code"],
                defaults={
                    **data,
                    "department": department,
                },
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created: {employee.employee_code}"
                    )
                )
            else:
                skipped_count += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped: {employee.employee_code} already exists"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Completed. Created: {created_count}, "
                f"Skipped: {skipped_count}"
            )
        )