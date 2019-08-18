from django.utils import timezone
from datetime import timedelta, date
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


class JobListingPublishViewTest(APITransactionTestCase):
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
            state=state
        )


class PublishJobListingsTests(JobListingPublishViewTest):

    def test_publish_job_listing(self):
        """
        This test asserts that a JobListing record can be prepared
        to be published, with a publish date and expiry date, when making
        a PUT request to the job-listings/publish/{id} endpoint.
        """

        request_body = {
            'date_to_publish': timezone.now(),
            'date_to_expire': date.today() + timedelta(days=1)
        }

        response = self.client.put(
            reverse("job-listing-publish", kwargs={'id': 1}),
            data=request_body
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        job_listing = JobListing.objects.get(id=1)
        self.assertEqual(job_listing.status, JobListingState.PREPUBLISH)
