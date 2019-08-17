from mixer.backend.django import mixer
from django.urls import reverse
from rest_framework.test import APITransactionTestCase, APIClient
from rest_framework.views import status
from ..models import JobListing
from ..enums import JobListingStatus
from apps.company.models import Company
from apps.common.models import (
    LocationStateCode,
    LocationCountryCode
)


class JobListingDeleteTest(APITransactionTestCase):
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
            status=JobListingStatus.DRAFT
        )

        mixer.blend(
            JobListing,
            company=company,
            country=country,
            state=state,
            status=JobListingStatus.PUBLISHED
        )


class DeleteJobListingTests(JobListingDeleteTest):

    def test_delete_draft_job_listing(self):
        """
        This test asserts that a specific JobListing record can be deleted
        when making a DELETE request to the job-listings/delete/{id} endpoint,
        if the JobListing record is a draft.
        """

        response = self.client.delete(
            reverse("job-listing-delete", kwargs={'id': 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRaises(JobListing.DoesNotExist, JobListing.objects.get, id=1)

    def test_delete_published_job_listing(self):
        """
        This test asserts that a specific JobListing record can NOT be deleted
        when making a DELETE request to the job-listings/delete/{id} endpoint,
        if the JobListing record is no longer a draft.
        """

        response = self.client.delete(
            reverse("job-listing-delete", kwargs={'id': 2})
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
