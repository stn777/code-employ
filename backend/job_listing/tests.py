from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import JobListing
from company.models import Company
from common.models import Location
from .serializers import JobListingSerializer
from .enums import JobPositionType, SalaryFrequency
from common.enums import LocationCountry, LocationState


class JobListingViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def create_job_listing(job_title, description, position_type, 
                           contract_length, salary, salary_frequency):
        JobListing.objects.create(
            company=Company.objects.get(id=1),
            job_title=job_title,
            description=description,
            location=Location.objects.get(id=1),
            position_type=position_type,
            contract_length=contract_length,
            salary=salary,
            salary_frequency=salary_frequency,
        )
    
    @classmethod
    def setUpTestData(cls):
        Location.objects.create(
            city="Melbourne",
            state=LocationState.VIC,
            country=LocationCountry.AU
        )

        Company.objects.create(
            legal_name="Test Company",
            email="company@email.com",
            website_url="http://some.website.com/",
            location=Location.objects.get(id=1),
        )

        cls.create_job_listing(
            "Senior Python Flask developer", 
            "Some description",
            JobPositionType.CONTRACT,
            12,
            850,
            SalaryFrequency.PERDAY,
        )
        cls.create_job_listing(
            "Mid-senior Python Flask developer",
            "Some description",
            JobPositionType.FULLTIME,
            None,
            110000,
            SalaryFrequency.PERYEAR
        )
        cls.create_job_listing(
            "Junior Golang Full-stack developer",
            "Some description",
            JobPositionType.CASUAL,
            None,
            40,
            SalaryFrequency.PERHOUR
        )


class JobListingsTests(JobListingViewTest):
    
    def test_get_job_listings(self):
        """
        This test asserts that all JobListing records added during 
        setUp are retrieved and serialized when making a GET request 
        to the job-listings endpoint.
        """
        
        response = self.client.get(
            reverse("job-listings-all")
        )

        expected = JobListing.objects.all()
        serialised = JobListingSerializer(expected, many=True)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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

