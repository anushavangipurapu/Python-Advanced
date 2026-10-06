from django.core.management.base import BaseCommand, CommandError

from employees.services import EmployeeCSVImportService


class Command(BaseCommand):
    help = "Import employees from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path",
            help="Path to the employee CSV file",
        )

    def handle(self, *args, **options):
        file_path = options["file_path"]

        try:
            result = EmployeeCSVImportService.import_csv(file_path)

        except FileNotFoundError:
            raise CommandError(
                f"CSV file not found: {file_path}"
            )

        except Exception as exc:
            raise CommandError(str(exc))

        self.stdout.write(
            self.style.SUCCESS(
                f"Import completed. "
                f"Created: {result['created']}, "
                f"Skipped: {result['skipped']}, "
                f"Failed: {result['failed']}"
            )
        )

        if result["errors"]:
            self.stdout.write("\nErrors:")

            for error in result["errors"]:
                self.stdout.write(
                    self.style.ERROR(error)
                )