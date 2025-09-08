from django.db import models

class CompanyModel(models.Model):
    company_id = models.CharField(max_length=25, primary_key=True)
    organization = models.ForeignKey("restapi.Organization", on_delete=models.CASCADE, null=True, blank=True, related_name="registered_companies")
    register = models.OneToOneField("restapi.RegisterModel", on_delete=models.CASCADE, unique=True, related_name="company_profile")
    company_name = models.CharField(max_length=100, blank=True)
    company_email = models.EmailField(blank=True, unique=True)

    def __str__(self):
        return self.register.get_full_name()
