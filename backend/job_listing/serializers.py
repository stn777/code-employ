from rest_framework import serializers
from .models import JobListing
from company.serializers import CompanySerializer
from common.serializers import (
    LocationSerializer, ProgrammingLanguageSerializer,
    PaginationFilterSerializer, PagedResponseSerializer
)


class JobListingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    location = LocationSerializer()
    languages = ProgrammingLanguageSerializer(many=True)

    class Meta:
        model = JobListing
        fields = '__all__'



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