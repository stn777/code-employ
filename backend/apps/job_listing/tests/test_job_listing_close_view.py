from mixer.backend.django import mixer
from django.urls import reverse
from rest_framework.test import APITransactionTestCase, APIClient
from rest_framework.views import status
from ..models import JobListing
from ..enums import JobListingState
from apps.company.models import Company
from apps.common.models import (
    LocationStateCode,
    LocationCountryCode
)


class JobListingCloseViewTest(APITransactionTestCase):
    client = APIClient()
    reset_sequences = True

    def setUp(self):
        country = mixer.blend(LocationCountryCode)
        state = mixer.blend(LocationStateCode, country_id=country.id)
        company = mixer.blend(Company, state_id=state.id, country_id=country.id)

        mixer.blend(
            JobListing,
            company=company,
            country=country,
            state=state,
            status=JobListingState.PUBLISHED
        )


class CloseJobListingsTests(JobListingCloseViewTest):

    def test_close_job_listing(self):
        """
        This test asserts that a JobListing record can be closed
        when making a PUT request to the job-listings/close/{id}
        endpoint.
        """

        response = self.client.put(
            reverse("job-listing-close", kwargs={'id': 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        job_listing = JobListing.objects.get(id=1)
        self.assertEqual(job_listing.status, JobListingState.CLOSED)
