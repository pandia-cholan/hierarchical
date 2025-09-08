from rest_framework import serializers
from restapi.models import RegisterModel

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterModel
        fields = ['username', 'usr_id', 'organization_id', 'company_id', 'email', 'first_name', 'last_name']