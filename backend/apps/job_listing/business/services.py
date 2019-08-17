from typing import List
from django_fsm import can_proceed
from rest_framework.exceptions import APIException
from apps.common.business.selectors import TagSelector
from .selectors import JobListingSelector
from ..models import JobListing, JobListingLanguage, JobListingTag
from ..enums import JobPositionType, SalaryFrequency, JobListingState
from ..api.serializers import (
    JobListingEditSerializer,
    JobListingPublishSerializer
)


class JobListingService():

    @staticmethod
    def create_job_listing(serializer: JobListingEditSerializer) -> int:
        new_listing = JobListing()
        id = JobListingService._save_job_listing(new_listing, serializer)
        return id

    @staticmethod
    def update_job_listing(id: int, serializer: JobListingEditSerializer) -> int:
        existing_listing = JobListingSelector.get_job_listing_by_id(id)
        JobListingService._save_job_listing(existing_listing, serializer)
        return id

    @staticmethod
    def delete_job_listing(id: int):
        job_listing = JobListingSelector.get_job_listing_by_id(id)
        if job_listing.status != JobListingState.DRAFT:
            raise APIException("Cannot delete this job listing, as it is no longer a draft.")
        JobListing.objects.get(id=id).delete()

    @staticmethod
    def pre_publish_job_listing(id: int, serializer: JobListingPublishSerializer):
        job_listing = JobListingSelector.get_job_listing_by_id(id)
        if not can_proceed(job_listing.pre_publish):
            raise APIException("Cannot prepare this job listing for publishing")
        job_listing.pre_publish()
        job_listing.save()

    @staticmethod
    def _save_job_listing(job_listing: JobListing, serializer: JobListingEditSerializer) -> int:
        job_listing.company_id = serializer.data.get('company_id')
        job_listing.job_title = serializer.data.get('job_title')
        job_listing.description = serializer.data.get('description')
        job_listing.position_type = JobPositionType(serializer.data.get('position_type'))
        job_listing.salary = serializer.data.get('salary')
        job_listing.salary_frequency = SalaryFrequency(serializer.data.get('salary_frequency'))
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
            tag, created = TagSelector.get_or_create_tag(tag_title)
            JobListingTag.objects.create(
                job_listing_id=job_listing_id,
                tag=tag
            )
