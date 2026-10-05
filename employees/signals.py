import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employee, EmployeeAuditLog


logger = logging.getLogger("employees")


@receiver(post_save, sender=Employee)
def employee_audit_log(sender, instance, created, **kwargs):
    try:
        if created:
            EmployeeAuditLog.objects.create(
                employee=instance,
                action="CREATE",
                changed_by=instance.user,
                changes={
                    "employee_code": instance.employee_code,
                    "first_name": instance.first_name,
                    "last_name": instance.last_name,
                    "department_id": instance.department_id,
                },
            )

            logger.info(
                "Employee audit created | action=CREATE | employee_id=%s",
                instance.id,
            )

        else:
            EmployeeAuditLog.objects.create(
                employee=instance,
                action="UPDATE",
                changed_by=instance.user,
                changes={
                    "employee_code": instance.employee_code,
                    "first_name": instance.first_name,
                    "last_name": instance.last_name,
                    "department_id": instance.department_id,
                },
            )

            logger.info(
                "Employee audit created | action=UPDATE | employee_id=%s",
                instance.id,
            )

    except Exception:
        logger.exception(
            "Employee audit failed | employee_id=%s",
            instance.id,
        )
        raise