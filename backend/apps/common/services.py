from django.http import Http404
from typing import List, Tuple
from .serializers import (
    LocationCountryCodeSerializer,
    LocationStateCodeSerializer
)
from .models import (
    LocationCountryCode, 
    LocationStateCode,
    ProgrammingLanguage,
    Tag
)


class LocationService():

    @staticmethod
    def get_country_codes() -> List[LocationCountryCode]:
        return LocationCountryCode.objects.all()

    @staticmethod
    def insert_country_code(country_code: LocationCountryCodeSerializer) -> int:
        country_code = LocationCountryCode(
            code=country_code.data['code'],
            name=country_code.data['name']
        )
        country_code.save()
        return country_code.pk

    @staticmethod
    def get_state_codes() -> List[LocationStateCode]:
        return LocationStateCode.objects.all()

    @staticmethod
    def insert_state_code(country_code_id: int, state_code: LocationStateCodeSerializer) -> int:
        state_code = LocationStateCode(
            country_id=country_code_id,
            code=state_code.data['code'],
            name=state_code.data['name']
        )
        state_code.save()
        return state_code.pk


class ProgrammingLanguageService():

    @staticmethod
    def get_programming_language_by_id(id: int) -> ProgrammingLanguage:
        try:
            return ProgrammingLanguage.objects.get(id=id)
        except ProgrammingLanguage.DoesNotExist:
            raise Http404(f'ProgrammingLanguage with id {id} could not be found')


class TagService():

    @staticmethod
    def get_or_create_tag(title: str) -> Tuple:
        return Tag.objects.get_or_create(title=title)