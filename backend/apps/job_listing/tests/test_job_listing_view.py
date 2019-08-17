from mixer.backend.django import mixer
from django.urls import reverse
from rest_framework.test import APITransactionTestCase, APIClient
from rest_framework.views import status
from ..models import JobListing
from ..api.serializers import JobListingSerializer
from apps.company.models import Company
from apps.common.models import (
    LocationStateCode,
    LocationCountryCode
)


class JobListingViewTest(APITransactionTestCase):
    client = APIClient()
    reset_sequences = True

    def setUp(self):
        country = mixer.blend(LocationCountryCode)
        state = mixer.blend(LocationStateCode, country_id=country.id)
        company = mixer.blend(Company, state_id=state.id, country_id=country.id)

        mixer.cycle(2).blend(
            JobListing,
            company=company,
            country=country,
            state=state,
        )


class GetJobListingsTests(JobListingViewTest):

    def test_get_job_listing_by_id(self):
        """
        This test asserts that a specific JobListing record added during
        setUp will be retrieved and serialized when making a GET request
        to the job-listings/{id} endpoint.
        """

        response = self.client.get(
            reverse("job-listing", kwargs={'id': 2})
        )

        expected = JobListing.objects.get(id=2)
        serialised = JobListingSerializer(expected)

        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
