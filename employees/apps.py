from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    name = "employees"

    def ready(self):
        import employees.signals
        import employees.monitoring_metrics