from .models import Company
from django.http import Http404


class CompanyService():

    @staticmethod
    def get_all_companies() -> list(Company):
        return Company.objects.all()

    @staticmethod
    def get_company_by_id(id: int) -> Company:
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist:
            raise Http404(f"Company with id {id} does not exist")