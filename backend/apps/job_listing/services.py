from django.http import Http404
from typing import List
from django.db.models import Q
from apps.common.utils import PagedResult
from apps.common.services import ProgrammingLanguageService, TagService
from .models import JobListing, JobListingLanguage, JobListingTag
from .enums import JobPositionType, SalaryFrequency
from .api.serializers import (
    JobListingSearchFilterSerializer, 
    JobListingEditSerializer
)


class JobListingService():

    @staticmethod
    def get_job_listing_by_id(id: int) -> JobListing:
        try:
            return JobListing.objects.get(id=id)
        except JobListing.DoesNotExist:
            raise Http404(f"JobListing with id {id} could not be found")

    @staticmethod
    def get_paged_job_listings(filter: JobListingSearchFilterSerializer) -> PagedResult:
        query = Q()

        if 'keyword' in filter.data:
            query &= (
                Q(job_title__contains=filter.data['keyword']) | 
                Q(description__contains=filter.data['keyword'])
            )
        if 'position_type' in filter.data:
            query &= Q(position_type=JobPositionType(filter.data['position_type']))
        if 'salary_min' in filter.data:
            query &= Q(salary__gte=filter.data['salary_min'])
        if 'salary_max' in filter.data:
            query &= Q(salary__lte=filter.data['salary_max'])
        if 'languages' in filter.data:
            query &= Q(languages__id__in=filter.data['languages'])

        job_listings = JobListing.objects.get_paginated(query, filter)
        record_count = JobListing.objects.all().count() 

        return PagedResult(items=job_listings, record_count=record_count)
    
    @staticmethod
    def create_job_listing(serializer: JobListingEditSerializer) -> int:
        new_listing = JobListing()
        id = JobListingService._save_job_listing(new_listing, serializer)
        return id

    @staticmethod
    def update_job_listing(id: int, serializer: JobListingEditSerializer) -> int:
        existing_listing = JobListingService.get_job_listing_by_id(id)
        JobListingService._save_job_listing(existing_listing, serializer)
        return id

    @staticmethod
    def _save_job_listing(job_listing: JobListing, serializer: JobListingEditSerializer) -> int:
        job_listing.company_id = serializer.data.get('company_id')
        job_listing.job_title = serializer.data.get('job_title')
        job_listing.description = serializer.data.get('description')
        job_listing.position_type = JobPositionType(serializer.data.get('position_type'))
        job_listing.salary = serializer.data.get('salary')
        job_listing.city = serializer.data.get('city')
        job_listing.country_id = serializer.data.get('country')
        job_listing.state_id = serializer.data.get('state')
        job_listing.post_code = serializer.data.get('post_code')
        
        job_listing.save()
        id = job_listing.pk

        languages = serializer.data.get('languages')
        JobListingService._save_job_listing_languages(id, languages)

        tags = serializer.data.get('tags')
        JobListingService._save_job_listing_tags(id, tags)

        return id

    @staticmethod
    def _save_job_listing_languages(job_listing_id: int, languages: List[int]):
        JobListingLanguage.objects.filter(job_listing_id=job_listing_id).delete()
        for language_id in languages:
            JobListingLanguage.objects.create(
                job_listing_id=job_listing_id,
                language_id=language_id
            )
    
    @staticmethod
    def _save_job_listing_tags(job_listing_id: int, tags: List[str]):
        JobListingTag.objects.filter(job_listing_id=job_listing_id).delete()
        for tag_title in tags:
            tag, created = TagService.get_or_create_tag(tag_title)
            JobListingTag.objects.create(
                job_listing_id=job_listing_id,
                tag=tag
            )
            