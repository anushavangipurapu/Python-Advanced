import csv

from django.core.management.base import BaseCommand

from employees.models import Employee


class Command(BaseCommand):
    help = "Export employees to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            default="employees.csv",
            help="Output CSV file path",
        )

    def handle(self, *args, **options):
        output_file = options["output"]

        employees = Employee.objects.select_related("department").all()

        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "employee_code",
                "first_name",
                "last_name",
                "email",
                "phone",
                "department",
                "designation",
                "salary",
                "joining_date",
                "role",
                "is_active",
            ])

            for employee in employees:
                writer.writerow([
                    employee.employee_code,
                    employee.first_name,
                    employee.last_name,
                    employee.email,
                    employee.phone,
                    employee.department.name,
                    employee.designation,
                    employee.salary,
                    employee.joining_date,
                    employee.role,
                    employee.is_active,
                ])

        self.stdout.write(
            self.style.SUCCESS(
                f"Employees exported successfully to {output_file}"
            )
        )