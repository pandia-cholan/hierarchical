from rest_framework.generics import  ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from restapi.models import RegisterModel, Organization, CompanyModel
from restapi.permissions import IsAuthenticatedOrganization, IsAuthenticatedCompany
from restapi.serializers import RegisterSerializer, CompanySerializer, EmployeeSerializer, OrganizationSerializer


class GetAllRegistered(ListAPIView):
    serializer_class = RegisterSerializer

    def get(self, request, *args, **kwargs):
        try:
            all_registered_models = RegisterModel.objects.all()
            registered_serializer = self.get_serializer(all_registered_models, many = True)
            return Response(registered_serializer.data)
        except Exception as e:
            return Response({"message" : str(e)})


class GetRegisterById(RetrieveAPIView):
    serializer_class = RegisterSerializer

    def get(self, request, *args, **kwargs):
        try:
            registered_user = RegisterModel.objects.get(pk = kwargs['pk'])
            return Response(self.get_serializer(registered_user).data)
        except RegisterModel.DoesNotExist:
            pk = kwargs['pk']
            return Response({"message" : f'{pk} is not available'})
        except Exception as e:
            return Response({"message" : str(e)})


class GetRegisteredCompanies(ListAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrganization,]

    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            organization = Organization.objects.get(register = user)
            companies = CompanyModel.objects.filter(organization = organization,register__is_company=True)
            serializer = self.get_serializer(companies, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message" : str(e)})


class GetRegisteredEmployees(ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedCompany]

    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            employees = RegisterModel.objects.filter(company = user.company, is_user = True)
            serializer = self.get_serializer(employees, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message" : str(e)})


class GetEmployeesByCompany(ListAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedCompany]

    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            company = CompanyModel.objects.get(register = user)
            serializer = self.get_serializer(company)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message" : str(e)})


class GetOrganizationAllSubs(RetrieveAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticatedOrganization]

    def get(self, request, *args, **kwargs):
        try:
            organization = Organization.objects.get(register=request.user)
            serializer = self.get_serializer(organization)
            return Response(serializer.data)
        except Organization.DoesNotExist:
            return Response({"message": "Organization not found"}, status=404)
        except Exception as e:
            return Response({"message": str(e)}, status=500)