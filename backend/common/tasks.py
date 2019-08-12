from celery import task
from .utils import make_http_get_request
from .service import LocationService
from .serializers import LocationCountryCodeSerializer, LocationStateCodeSerializer
from django.conf import settings
from code_employ import celery_app


@celery_app.task(bind=True, max_retries=settings.CELERY_MAX_RETRIES)
def sync_country_codes(self):
    response = make_http_get_request(settings.COUNTRY_CODE_API_URL)
    countries = response.json()['result']

    existing_countries = LocationService.get_country_codes()
    existing_states = LocationService.get_state_codes()

    for country in countries:
        existing_country = next((existing for existing in existing_countries 
                                if existing.code == country['code']), None)
        if existing_country:
            if country['name'] != existing_country.name:
                serialized = LocationCountryCodeSerializer(country)
                LocationService.update_country_code(serialized, existing_country.id)
            
            for state in country['states'] or []:
                existing_state = next((existing for existing in existing_states
                                       if existing.code == state['code'] and existing.country.code 
                                       == existing_country.code), None)
                if existing_state:
                    if state['name'] != existing_state.name:
                        serialized = LocationStateCodeSerializer(state)
                        LocationService.update_state_code(serialized, existing_state.id)
                else:
                   serialized = LocationStateCodeSerializer(state)
                   LocationService.insert_state_code(existing_country, serialized) 
        else:
            serialized = LocationCountryCodeSerializer(country)
            LocationService.insert_country_code(serialized)


