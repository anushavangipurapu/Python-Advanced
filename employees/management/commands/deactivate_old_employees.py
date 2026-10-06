from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from employees.models import Employee


class Command(BaseCommand):
    help = "Deactivate employees who have been inactive for more than 1 year"

    def handle(self, *args, **options):
        cutoff_date = timezone.now().date() - timedelta(days=365)

        employees = Employee.objects.filter(
            is_active=True,
            joining_date__lt=cutoff_date,
        )

        count = employees.update(is_active=False)

        self.stdout.write(
            self.style.SUCCESS(
                f"Deactivated {count} old employee(s)."
            )
        )