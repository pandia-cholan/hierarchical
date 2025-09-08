from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView, LogoutView as KnoxLogoutView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class LoginView(KnoxLoginView, CreateAPIView):
    serializer_class = AuthTokenSerializer
    permission_classes = [AllowAny,]

    def post(self, request, format=None):
        try:
            login_serializer = self.get_serializer(data = request.data)
            if login_serializer.is_valid():
                login(request, login_serializer.validated_data['user'])
                return super().post(request=request)
            else:
                return Response(login_serializer.errors)
        except Exception as e:
            return Response({"message" : str(e)})


class LogoutView(KnoxLogoutView):

    def post(self, request, format=None):
        return super().post(request=request)