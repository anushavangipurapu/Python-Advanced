from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees"
    )
    projects = models.ManyToManyField(
    "Project",
    related_name="employees",
    blank=True
)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeProfile(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)
    profile_image = models.ImageField(
        upload_to="employee_profiles/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.employee_code} Profile"


class Project(models.Model):
    name = models.CharField(max_length=200)
    project_code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    client_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name