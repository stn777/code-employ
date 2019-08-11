from rest_framework import serializers
from .models import JobListing
from company.serializers import CompanySerializer
from common.serializers import (
    ProgrammingLanguageSerializer, PaginationFilterSerializer, 
    PagedResponseSerializer, LocationStateCodeSerializer,
    LocationCountryCodeSerializer
)


class JobListingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    state = LocationStateCodeSerializer()
    country = LocationCountryCodeSerializer()
    languages = ProgrammingLanguageSerializer(many=True)

    class Meta:
        model = JobListing
        fields = '__all__'


class JobListingEditSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    job_title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    location_same_as_company = serializers.BooleanField(default=False)
    position_type = serializers.IntegerField()
    contract_length = serializers.IntegerField()
    salary = serializers.IntegerField()
    salary_frequency = serializers.IntegerField()
    language_ids = serializers.ListField(
        child=serializers.IntegerField()
    ),
    tags = serializers.ListField(
        child=serializers.CharField(max_length=40)
    )


class JobListingSearchFilterSerializer(PaginationFilterSerializer):
    keyword = serializers.CharField(max_length=100, required=False)
    languages = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )
    position_type = serializers.IntegerField(required=False)
    salary_min = serializers.IntegerField(required=False)
    salary_max = serializers.IntegerField(required=False)


class JobListingSearchResponseSerializer(PagedResponseSerializer):
    items = JobListingSerializer(many=True)
