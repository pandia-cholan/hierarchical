from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from restapi.models import RegisterModel
from restapi.permissions import IsAuthenticatedCompany
from restapi.serializers import RegisterSerializer
from restapi.views.IdGenerator import generate_user_id

class RegisterEmployee(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticatedCompany, ]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                print(validated_data)
                validated_data['usr_id'] = generate_user_id()
                validated_data['password'] = make_password(validated_data['password'])
                user_fields = {
                    key: validated_data[key] for key in [
                        'usr_id', 'first_name', 'last_name', 'email', 'username',
                        'password', "is_user"
                    ] if key in validated_data
                }
                new_register = RegisterModel.objects.create(**user_fields)
                company = request.user.company
                new_register.organization = company.organization
                new_register.company = company
                new_register.save()
                return Response({"message": "created employee"})
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({"message": str(e)})



