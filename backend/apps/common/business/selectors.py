from django.http import Http404
from typing import List, Tuple
from ..models import (
    LocationStateCode, LocationCountryCode,
    ProgrammingLanguage, Tag
)


class LocationSelector():

    @staticmethod
    def get_country_codes() -> List[LocationCountryCode]:
        return LocationCountryCode.objects.all()

    @staticmethod
    def get_state_codes() -> List[LocationStateCode]:
        return LocationStateCode.objects.all()


class ProgrammingLanguageSelector():

    @staticmethod
    def get_programming_language_by_id(id: int) -> ProgrammingLanguage:
        try:
            return ProgrammingLanguage.objects.get(id=id)
        except ProgrammingLanguage.DoesNotExist:
            raise Http404(f'ProgrammingLanguage with id {id} could not be found')


class TagSelector():

    @staticmethod
    def get_or_create_tag(title: str) -> Tuple:
        return Tag.objects.get_or_create(title=title)
