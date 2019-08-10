from rest_framework import serializers
from .models import Location, ProgrammingLanguage


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = '__all__'


class PaginationFilterSerializer(serializers.Serializer):
    current_page = serializers.IntegerField()
    items_per_page = serializers.IntegerField()
    order_by_column = serializers.CharField(max_length=100, default='id')
    order_direction = serializers.BooleanField(default=False)


class PagedResponseSerializer(serializers.Serializer):
    record_count = serializers.IntegerField()