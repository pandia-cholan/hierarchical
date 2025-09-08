from rest_framework import serializers
from restapi.models import CompanyModel
from restapi.serializers.EmployeeSerializer import EmployeeSerializer


class CompanySerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField(read_only=True)
    employees_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CompanyModel
        fields = ['company_name', 'company_email', 'company_id',  'employees_count', 'employees']

    def get_employees(self, obj):
        employees_qs = obj.company_employees.filter(is_user=True)
        return EmployeeSerializer(employees_qs, many=True).data

    def get_employees_count(self, obj):
        return obj.company_employees.filter(is_user = True).count()