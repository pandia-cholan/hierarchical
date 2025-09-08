from rest_framework.permissions import BasePermission

class IsAuthenticatedOrganization(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'organization'

class IsAuthenticatedCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'company'

class IsAuthenticatedEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employee'


