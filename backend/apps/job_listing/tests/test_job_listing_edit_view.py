from mixer.backend.django import mixer
from django.urls import reverse
from rest_framework.test import APITransactionTestCase, APIClient
from rest_framework.views import status
from ..models import JobListing
from apps.company.models import Company
from apps.common.models import (
    LocationStateCode,
    LocationCountryCode,
    ProgrammingLanguage
)


class JobListingEditTest(APITransactionTestCase):
    client = APIClient()
    reset_sequences = True

    def setUp(self):
        country = mixer.blend(LocationCountryCode)
        state = mixer.blend(LocationStateCode, country_id=country.id)
        company = mixer.blend(Company, state_id=state.id, country_id=country.id)
        ProgrammingLanguage.objects.create(name="Python")

        mixer.blend(
            JobListing,
            job_title='Python developer',
            company_id=company.id,
            country_id=country.id,
            state_id=state.id,
        )


class EditJobListingTests(JobListingEditTest):

    def test_post_job_listing(self):
        """
        This test asserts that a JobListing record can be created
        by making a POST request to the job-listings/new endpoint.
        """

        request_body = {
            'company_id': 1,
            'job_title': 'Python developer',
            'description': 'Some description',
            'position_type': 1,
            'salary': 49000,
            'salary_frequency': 1,
            'country': 1,
            'state': 1,
            'city': 'Sydney',
            'post_code': 2000,
            'languages': [1],
            'tags': ['python']
        }

        response = self.client.post(
            reverse("job-listing-new"), data=request_body
        )

        expected = JobListing.objects.get(id=2)

        self.assertIsNotNone(expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_job_listing(self):
        """
        This test asserts that an existing JobListing record can be updated
        by making a PUT request to the job-listings/edit endpoint
        """

        request_body = {
            'company_id': 1,
            'job_title': 'Java developer',
            'description': 'Some description',
            'position_type': 2,
            'salary': 84000,
            'salary_frequency': 1,
            'country': 1,
            'state': 1,
            'city': 'Melbourne',
            'post_code': 2000,
            'languages': [1],
            'tags': ["python"]
        }

        existing = JobListing.objects.get(id=1)
        self.assertEqual(existing.job_title, 'Python developer')

        response = self.client.put(
            reverse("job-listing-edit", kwargs={'id': 1}),
            data=request_body
        )

        existing = JobListing.objects.get(id=1)
        self.assertEqual(existing.job_title, 'Java developer')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
