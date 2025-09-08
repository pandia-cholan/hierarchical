from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from restapi.models import RegisterModel
from restapi.models.OrganizationModel import Organization
from restapi.permissions import IsAuthenticatedOrganization
from restapi.serializers import RegisterSerializer, OrganizationSerializer
from restapi.views.IdGenerator import generate_user_id, generate_organization_id

class RegisterOrganization(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                print(validated_data)
                validated_data['usr_id'] = generate_user_id()
                validated_data['password'] = make_password(validated_data['password'])
                validated_data['role'] = 'organization'
                if validated_data['is_organization']:

                    user_fields = {
                        key: validated_data[key] for key in [
                            'usr_id', 'first_name', 'last_name', 'email','username',
                            'password','is_organization', 'role'
                        ] if key in validated_data
                    }
                    new_register = RegisterModel.objects.create(**user_fields)
                    new_register.save()

                    organization_fields = {
                        key: validated_data[key] for key in ['organization_name', 'organization_email']
                        if key in validated_data
                    }
                    organization_fields['organization_id'] = generate_organization_id()
                    organization_fields['register'] = new_register
                    new_organization = Organization.objects.create(**organization_fields)
                    new_organization.save()
                    new_register.organization = new_organization
                    new_register.save()
                    return Response({"message": "created organization"})
                else:
                    return Response({"message": "it is not organization"})
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({"message": str(e)})


