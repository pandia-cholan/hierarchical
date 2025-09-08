from restapi.models import RegisterModel, CompanyModel
from restapi.models.OrganizationModel import Organization

def generate_user_id():
    last_user = RegisterModel.objects.order_by('-usr_id').first()
    new_id = 1
    if last_user and last_user.usr_id:
        new_id = int(last_user.usr_id[3:]) + 1
    new_user_id = f'usr{new_id:04d}'
    print(new_user_id)
    return new_user_id


def generate_organization_id():
    last_organization = Organization.objects.order_by('-organization_id').first()
    new_id = 1
    if last_organization and last_organization.organization_id:
        new_id = int(last_organization.organization_id[3:]) + 1
    new_organization_id = f'org{new_id:04d}'
    print(new_organization_id)
    return new_organization_id


def generate_company_id():
    last_company = CompanyModel.objects.order_by('-company_id').first()
    new_id = 1
    if last_company and last_company.company_id:
        new_id = int(last_company.company_id[4:]) + 1
    new_company_id = f'comp{new_id:04d}'
    print(new_company_id)
    return new_company_id



