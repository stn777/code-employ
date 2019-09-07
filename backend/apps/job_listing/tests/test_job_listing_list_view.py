from mixer.backend.django import mixer
from django.urls import reverse
from django.db.models import Q
from rest_framework.test import APITransactionTestCase, APIClient
from rest_framework.views import status
from ..models import JobListing, JobListingLanguage
from ..api.serializers import JobListingSearchResponseSerializer
from ..enums import JobPositionType, SalaryFrequency
from apps.company.models import Company
from apps.core.managers import PagedResult
from apps.common.models import (
    LocationStateCode,
    LocationCountryCode,
    ProgrammingLanguage
)


class JobListingListViewTest(APITransactionTestCase):
    client = APIClient()
    reset_sequences = True

    @staticmethod
    def create_job_listing(company_id, job_title, description, country_id,
                           state_id, position_type, contract_length, salary,
                           salary_frequency, language_id):
        job_listing = JobListing.objects.create(
            company_id=company_id,
            job_title=job_title,
            description=description,
            city='Sydney',
            state_id=state_id,
            country_id=country_id,
            post_code='2000',
            position_type=position_type,
            contract_length=contract_length,
            salary=salary,
            salary_frequency=salary_frequency,
        )

        JobListingLanguage.objects.create(
            job_listing_id=job_listing.id,
            language_id=language_id
        )

    def setUp(self):
        country = mixer.blend(LocationCountryCode)
        state = mixer.blend(LocationStateCode, country_id=country.id)
        company = mixer.blend(
            Company,
            state_id=state.id,
            country_id=country.id
        )

        python = mixer.blend(ProgrammingLanguage, name='Python')
        golang = mixer.blend(ProgrammingLanguage, name='Golang')

        self.create_job_listing(
            company.id,
            'Senior Python Django developer',
            'Some description',
            country.id,
            state.id,
            JobPositionType.CONTRACT,
            12,
            850,
            SalaryFrequency.PERDAY,
            python.id
        )

        self.create_job_listing(
            company.id,
            'Mid-senior Python Flask developer',
            'Some description',
            country.id,
            state.id,
            JobPositionType.FULLTIME,
            None,
            110000,
            SalaryFrequency.PERYEAR,
            python.id
        )

        self.create_job_listing(
            company.id,
            'Junior Golang Full-stack developer',
            'Some description',
            country.id,
            state.id,
            JobPositionType.CASUAL,
            None,
            40,
            SalaryFrequency.PERHOUR,
            golang.id
        )


class GetJobListingListTests(JobListingListViewTest):

    def test_paged_job_listings_no_filter(self):
        """
        This test asserts that all Job Listings are returned through the
        job-listings/paged endpoint in a paginated list all filtering options
        are left default.
        """

        request_body = {
            'current_page': 1,
            'items_per_page': 20,
            'order_direction': True
        }

        response = self.client.post(
            reverse('job-listings-paged'),
            data=request_body
        )

        expected_items = JobListing.objects.all()[0:20]
        expected_count = JobListing.objects.all().count()

        expected_result = PagedResult(
            items=expected_items,
            record_count=expected_count
        )

        serialised = JobListingSearchResponseSerializer(expected_result)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(len(response.data['items']), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_paged_job_listings_filter(self):
        """
        This test asserts that the appropriate Job Listings are returned
        through the job-listings/paged endpoint in a paginated list when
        combining all filter options.
        """

        keyword_filter = 'developer'
        language_filter = [1]
        position_type_filter = JobPositionType.CONTRACT.value
        salary_min_filter = 0
        salary_max_filter = 850

        request_body = {
            'keyword': keyword_filter,
            'languages': language_filter,
            'position_type': position_type_filter,
            'salary_min': salary_min_filter,
            'salary_max': salary_max_filter,
            'current_page': 1,
            'items_per_page': 20,
            'order_direction': True
        }

        response = self.client.post(
            reverse('job-listings-paged'),
            data=request_body
        )

        expected_filter = (
            (Q(job_title__contains=keyword_filter) |
             Q(description__contains=keyword_filter)) &
            Q(languages__id__in=language_filter) &
            Q(position_type=JobPositionType(position_type_filter)) &
            Q(salary__gte=salary_min_filter) &
            Q(salary__lte=salary_max_filter)
        )

        expected_items = JobListing.objects.filter(expected_filter)[0:20]
        expected_count = JobListing.objects.all().count()

        expected_result = PagedResult(
            items=expected_items,
            record_count=expected_count
        )

        serialised = JobListingSearchResponseSerializer(expected_result)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.data['items'][0]['id'], 1)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_paged_job_listings_order_by(self):
        """
        This test asserts that paginated results returned through the
        job-listings/paged endpoint will be ordered by the appropriate
        sort_by_column value, and will be ordered in either ascending or
        descending order, depending on the order_direction value provided.
        """

        request_body = {
            'order_by_column': 'salary',
            'current_page': 1,
            'items_per_page': 20,
            'order_direction': False
        }

        response = self.client.post(
            reverse('job-listings-paged'),
            data=request_body
        )

        expected_items = JobListing.objects.all().order_by('-salary')[0:20]
        expected_count = JobListing.objects.all().count()

        expected_result = PagedResult(
            items=expected_items,
            record_count=expected_count
        )

        serialised = JobListingSearchResponseSerializer(expected_result)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.data['items'][0]['salary'], 110000)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
