from rest_framework import serializers

from restapi.models import RegisterModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterModel
        fields = ['first_name', 'last_name' ,'role']