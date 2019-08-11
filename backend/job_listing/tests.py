from django.urls import reverse
from django.test import TestCase
from django.db.models import Q
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import JobListing, JobListingLanguage
from .enums import JobPositionType, SalaryFrequency
from company.models import Company
from common.utils import PagedResult
from common.models import (
    LocationStateCode, 
    LocationCountryCode,
    ProgrammingLanguage
)
from .serializers import (
    JobListingSerializer, JobListingSearchResponseSerializer
)


class JobListingViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_job_listing(job_title, description, position_type, contract_length, 
                           salary, salary_frequency, language_id):
        job_listing = JobListing.objects.create(
            company=Company.objects.get(id=1),
            job_title=job_title,
            description=description,
            city='Sydney',
            state=LocationStateCode.objects.get(id=1),
            country=LocationCountryCode.objects.get(id=1),
            post_code='2000',
            position_type=position_type,
            contract_length=contract_length,
            salary=salary,
            salary_frequency=salary_frequency,
        )

        JobListingLanguage.objects.create(
            job_listing=JobListing.objects.get(id=job_listing.id),
            language=ProgrammingLanguage.objects.get(id=language_id)
        )
    
    @classmethod
    def setUpTestData(cls):
        country = LocationCountryCode.objects.create(
            code="AU",
            name="Australia"
        )

        state = LocationStateCode.objects.create(
            country=LocationCountryCode.objects.get(id=country.id),
            code="NSW",
            name="New South Wales"
        )

        Company.objects.create(
            legal_name="Test Company",
            email="company@email.com",
            website_url="http://some.website.com/",
            city='Sydney',
            state=LocationStateCode.objects.get(id=state.id),
            country=LocationCountryCode.objects.get(id=country.id),
            post_code='2000'
        )

        python = ProgrammingLanguage.objects.create(
            name="Python"
        )

        golang = ProgrammingLanguage.objects.create(
            name="Golang"
        )

        cls.create_job_listing(
            "Senior Python Django developer",
            "Some description",
            JobPositionType.CONTRACT,
            12,
            850,
            SalaryFrequency.PERDAY,
            python.id
        )

        cls.create_job_listing(
            "Mid-senior Python Flask developer",
            "Some description",
            JobPositionType.FULLTIME,
            None,
            110000,
            SalaryFrequency.PERYEAR,
            python.id
        )

        cls.create_job_listing(
            "Junior Golang Full-stack developer",
            "Some description",
            JobPositionType.CASUAL,
            None,
            40,
            SalaryFrequency.PERHOUR,
            golang.id
        )


class GetJobListingsTests(JobListingViewTest):

    def test_get_job_listing_by_id(self):
        """
        This test asserts that a specific JobListing record added during
        setUp will be retrieved and serialized when making a GET request
        to the job-listings/{id} endpoint.
        """

        response = self.client.get(
            reverse("job-listing", kwargs={'id':2})
        )

        expected = JobListing.objects.get(id=2)
        serialised = JobListingSerializer(expected)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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
            reverse("job-listings-paged"),
            data=request_body
        )
        
        expected_items = JobListing.objects.all()[0:20]
        expected_count = JobListing.objects.all().count()
        
        expected_result = PagedResult(items=expected_items, record_count=expected_count)
        serialised = JobListingSearchResponseSerializer(expected_result)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(len(response.data['items']), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_paged_job_listings_filter(self):
        """
        This test asserts that the appropriate Job Listings are returned through
        the job-listings/paged endpoint in a paginated list when combining all 
        filter options.
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
            reverse("job-listings-paged"),
            data=request_body
        )
        
        expected_filter = (
            (Q(job_title__contains=keyword_filter) | Q(description__contains=keyword_filter)) &
            Q(languages__id__in=language_filter) &
            Q(position_type=JobPositionType(position_type_filter)) &
            Q(salary__gte=salary_min_filter) &
            Q(salary__lte=salary_max_filter)
        )
        
        expected_items = JobListing.objects.filter(expected_filter)[0:20]
        expected_count = JobListing.objects.all().count()

        expected_result = PagedResult(items=expected_items, record_count=expected_count)
        serialised = JobListingSearchResponseSerializer(expected_result)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.data['items'][0]['id'], 1)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_paged_job_listings_order_by(self):
        """
        This test asserts that paginated results returned through the job-listings/paged
        endpoint will be ordered by the appropriate sort_by_column value, and will be ordered
        in either ascending or descending order, depending on the order_direction
        value provided.
        """

        request_body = {
            'order_by_column': 'salary',
            'current_page': 1,
            'items_per_page': 20,
            'order_direction': False
        }

        response = self.client.post(
            reverse("job-listings-paged"),
            data=request_body
        )
        
        expected_items = JobListing.objects.all().order_by('-salary')[0:20]
        expected_count = JobListing.objects.all().count()
        
        expected_result = PagedResult(items=expected_items, record_count=expected_count)
        serialised = JobListingSearchResponseSerializer(expected_result)
        
        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.data['items'][0]['salary'], 110000)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
