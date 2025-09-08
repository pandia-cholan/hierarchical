from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)
    organization_id = serializers.CharField(required=False, allow_null=True)
    company_id = serializers.CharField(required=False, allow_null=True)
    is_company = serializers.BooleanField(required=False, default=False)
    is_organization = serializers.BooleanField(required=False, default=False)
    is_user = serializers.BooleanField(required=False, default=False)
    organization_name = serializers.CharField(required=False,max_length=50)
    organization_email = serializers.EmailField(required=False)
    company_name = serializers.CharField(required=False, max_length=50)
    company_email = serializers.EmailField(required=False)

    def validate_password(self, data):
        if len(data) < 8:
            return serializers.ValidationError("password must be greater or equal to 8")
        return data
