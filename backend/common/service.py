from .models import LocationCountryCode, LocationStateCode


class LocationService():

    @staticmethod
    def get_country_codes():
        return LocationCountryCode.objects.all()

    @staticmethod
    def insert_country_code(country_code):
        country_code = LocationCountryCode(
            code=country_code.data['code'],
            name=country_code.data['name']
        )
        country_code.save()

    @staticmethod
    def update_country_code(country_code, id):
        existing = LocationCountryCode.objects.get(id=id)
        existing.code = country_code.data['code']
        existing.name = country_code.data['name']
        existing.save()

    @staticmethod
    def get_state_codes():
        return LocationStateCode.objects.all()

    @staticmethod
    def insert_state_code(country_code, state_code):
        state_code = LocationStateCode(
            country=country_code,
            code=state_code.data['code'],
            name=state_code.data['name']
        )
        state_code.save()

    @staticmethod
    def update_state_code(state_code, id):
        existing = LocationStateCode.objects.get(id=id)
        existing.code = state_code.data['code']
        existing.name = state_code.data['name']