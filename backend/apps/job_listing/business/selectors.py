from typing import List
from datetime import datetime, timedelta
from django.http import Http404
from django.db.models import Q
from apps.core.managers import PagedResult
from ..enums import JobPositionType, JobListingState
from ..models import JobListing, JobListingList
from ..api.serializers import JobListingSearchFilterSerializer


class JobListingSelector():

    @staticmethod
    def get_job_listing_by_id(id: int) -> JobListing:
        try:
            return JobListing.objects.get(id=id)
        except JobListing.DoesNotExist:
            raise Http404(f"JobListing with id {id} could not be found")

    @staticmethod
    def get_job_listings_by_status(status: JobListingState) -> List[JobListing]:
        return JobListing.objects.filter(status=status).all()

    @staticmethod
    def get_job_listings_ready_for_publish() -> List[JobListing]:
        return JobListing.objects.filter(
            Q(status=JobListingState.PREPUBLISH) &
            Q(date_to_publish__lte=datetime.now())
        )

    @staticmethod
    def get_job_listings_ready_for_expiry() -> List[JobListing]:
        return JobListing.objects.filter(
            Q(status=JobListingState.PUBLISHED) &
            Q(date_to_expire__lte=datetime.now())
        )

    @staticmethod
    def get_job_listings_ready_for_archive() -> List[JobListing]:
        return JobListing.objects.filter(
            (Q(status=JobListingState.CLOSED) |
             Q(status=JobListingState.EXPIRED)) &
            Q(date_closed__lte=(datetime.now() - timedelta(days=30)))
        )

    @staticmethod
    def get_paged_job_listings(filter: JobListingSearchFilterSerializer) -> PagedResult:
        query = Q()

        if 'keyword' in filter.data:
            query &= (
                Q(job_title__contains=filter.data['keyword']) |
                Q(description__contains=filter.data['keyword'])
            )
        if 'position_type' in filter.data:
            query &= Q(position_type=JobPositionType(
                filter.data['position_type']))
        if 'salary_min' in filter.data:
            query &= Q(salary__gte=filter.data['salary_min'])
        if 'salary_max' in filter.data:
            query &= Q(salary__lte=filter.data['salary_max'])
        if 'languages' in filter.data:
            query &= Q(languages__contained_by=filter.data['languages'])

        return JobListingList.objects.get_paginated(query, filter)
