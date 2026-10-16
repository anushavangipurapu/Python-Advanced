
from django.test import TestCase
from django.db import transaction
from employees.models import Department


class CeleryRollbackTest(TestCase):

    def test_database_changes_rollback_on_error(self):
        department_code = "ROLLBACK-TEST"

        self.assertFalse(
            Department.objects.filter(
                code=department_code
            ).exists()
        )

        with self.assertRaises(RuntimeError):
            with transaction.atomic():
                Department.objects.create(
                    name="Rollback Test Department",
                    code=department_code,
                )

                raise RuntimeError("Intentional rollback test")

        self.assertFalse(
            Department.objects.filter(
                code=department_code
            ).exists()
        )
