from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AnonymousUser
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from restapi.models import RegisterModel, CompanyModel
from restapi.permissions import IsAuthenticatedOrganization
from restapi.serializers import RegisterSerializer
from restapi.views.IdGenerator import generate_user_id, generate_company_id


class RegisterCompany(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticatedOrganization, ]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            password = serializer.data['password']
            if len(password) < 8:
                return Response({'message' : "password must be gerater than 8"}, status=400)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                print(validated_data)
                validated_data['usr_id'] = generate_user_id()
                validated_data['password'] = make_password(validated_data['password'])
                validated_data['role'] = 'company'
                if validated_data['is_company']:
                    
                    user_fields = {
                        key: validated_data[key] for key in [
                            'usr_id', 'first_name', 'last_name', 'email', 'username',
                            'password', 'is_company','role'
                        ] if key in validated_data
                    }
                    new_register = RegisterModel.objects.create(**user_fields)
                    new_register.save()

                    company_fields = {
                        key: validated_data[key] for key in ['company_name', 'company_email']
                        if key in validated_data
                    }

                    company_fields['company_id'] = generate_company_id()
                    company_fields['register'] = new_register
                    new_company = CompanyModel.objects.create(**company_fields)
                    organization = request.user.organization
                    new_company.organization = organization
                    new_company.save()
                    new_register.organization = organization
                    new_register.company = new_company
                    new_register.save()
                    return Response({"message": "created company"})
                else:
                    return Response({"message": "it is not company"})
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({"message": str(e)})



