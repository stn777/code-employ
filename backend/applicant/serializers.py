from rest_framework import serializers
from .models import JobListing


class ApplicantSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    location = LocationSerializer()
    languages = ProgrammingLanguageSerializer(many=True)

    class Meta:
        model = JobListing
        fields = '__all__'
