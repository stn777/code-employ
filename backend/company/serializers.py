from rest_framework import serializers
from common.serializers import LocationSerializer
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Company
        fields = '__all__'
