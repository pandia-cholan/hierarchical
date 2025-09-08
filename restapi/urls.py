from django.urls import path, include
from restapi.views import GetAllRegistered, GetRegisterById, LoginView, LogoutView, RegisterOrganization, \
    RegisterEmployee, GetEmployeesByCompany, GetOrganizationAllSubs
from restapi.views.CompanyView import RegisterCompany

urlpatterns = [
    path('register/', include([
        path('organization/', RegisterOrganization.as_view()),
        path('company/', RegisterCompany.as_view()),
        path('employee/', RegisterEmployee.as_view()),
    ])),
    path('get/', include([
        path('all/', GetAllRegistered.as_view()),
        path('<str:pk>/', GetRegisterById.as_view()),
    ])),
    path('', include([
        path('login/', LoginView.as_view()),
        path('logout/', LogoutView.as_view())
    ])),
    path("getcomp/", GetEmployeesByCompany.as_view()),
    path("getorg/", GetOrganizationAllSubs.as_view())
]

