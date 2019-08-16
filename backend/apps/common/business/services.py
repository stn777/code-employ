from ..api.serializers import (
    LocationCountryCodeSerializer,
    LocationStateCodeSerializer
)
from ..models import (
    LocationCountryCode,
    LocationStateCode
)


class LocationService():

    @staticmethod
    def insert_country_code(country_code: LocationCountryCodeSerializer) -> int:
        country_code = LocationCountryCode(
            code=country_code.data['code'],
            name=country_code.data['name']
        )
        country_code.save()
        return country_code.pk

    @staticmethod
    def insert_state_code(country_code_id: int, state_code: LocationStateCodeSerializer) -> int:
        state_code = LocationStateCode(
            country_id=country_code_id,
            code=state_code.data['code'],
            name=state_code.data['name']
        )
        state_code.save()
        return state_code.pk
