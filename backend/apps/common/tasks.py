import pycountry
from celery import shared_task
from .service import LocationService
from .serializers import LocationCountryCodeSerializer, LocationStateCodeSerializer
from django.conf import settings
from code_employ.celery import TransactionTask


@shared_task(base=TransactionTask, bind=True, max_retries=settings.CELERY_MAX_RETRIES)
def insert_country_codes(self):
    existing_countries = LocationService.get_country_codes()
    existing_states = LocationService.get_state_codes()

    for country in pycountry.countries:
        if not any(existing.code == country.alpha_2 for existing in existing_countries):  
            serialized_country = LocationCountryCodeSerializer(
                {
                    'code':country.alpha_2,
                    'name':country.name
                }
            )
            new_country = LocationService.insert_country_code(serialized_country)
            for subdivision in pycountry.subdivisions.get(country_code=new_country.code):
                if not any(existing.code == subdivision.code for existing in existing_states):
                    serialized_state = LocationCountryCodeSerializer(
                        {
                            'code':subdivision.code,
                            'name':subdivision.name,
                            'type':subdivision.type
                        }
                    )
                new_state = LocationService.insert_state_code(new_country, serialized_state)

