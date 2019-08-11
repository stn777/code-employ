from rest_framework import serializers
from .models import Company
from common.serializers import (
    LocationStateCodeSerializer,
    LocationCountryCodeSerializer
)


class CompanySerializer(serializers.ModelSerializer):
    state = LocationStateCodeSerializer()
    country = LocationCountryCodeSerializer()
    class Meta:
        model = Company
        fields = '__all__'
