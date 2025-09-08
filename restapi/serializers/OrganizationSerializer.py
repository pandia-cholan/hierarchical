from rest_framework import serializers
from restapi.models import Organization
from restapi.serializers.CompanySerializer import CompanySerializer

class OrganizationSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(source='registered_companies', many=True, read_only=True)
    companies_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Organization
        fields = ['organization_id', 'organization_name', 'organization_email', 'companies_count', 'companies']

    def get_companies(self, obj):
        companies = obj.registered_companies.all()
        return CompanySerializer(companies, many=True).data

    def get_companies_count(self, obj):
        return obj.registered_companies.count()