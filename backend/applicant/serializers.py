from rest_framework import serializers
from .models import Applicant
from company.serializers import CompanySerializer
from common.serializers import (
    ProgrammingLanguageSerializer,
    LocationStateCodeSerializer,
    LocationCountryCodeSerializer
)


class ApplicantSerializer(serializers.ModelSerializer):
    state = LocationStateCodeSerializer()
    country = LocationCountryCodeSerializer()
    languages = ProgrammingLanguageSerializer(many=True)

    class Meta:
        model = Applicant
        fields = '__all__'
