from django.contrib.auth.models import AbstractUser
from django.db import models

class RegisterModel(AbstractUser):
    ROLE_CHOICES = [
        ('organization', 'Organization'),
        ('company', 'Company'),
        ('employee', 'Employee'),
    ]
    usr_id = models.CharField(max_length=25, primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="employee")
    organization = models.ForeignKey("restapi.Organization", on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name="registered_users")
    company = models.ForeignKey("restapi.CompanyModel", on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="company_employees")
    is_company = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_full_name()}"
