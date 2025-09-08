from django.db import models

class Organization(models.Model):
    organization_id = models.CharField(max_length=25, primary_key=True)
    register = models.OneToOneField("restapi.RegisterModel", on_delete=models.CASCADE, unique=True, related_name="organization_profile")
    organization_name = models.CharField(max_length=100, blank=True)
    organization_email = models.EmailField(blank=True, unique=True)

    def __str__(self):
        return self.register.get_full_name()
