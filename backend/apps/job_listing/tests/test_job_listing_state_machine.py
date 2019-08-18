from mixer.backend.django import mixer
from datetime import datetime, date, timedelta
from django_fsm import can_proceed
from django.test import TestCase
from ..models import JobListing
from ..enums import JobListingState
from apps.company.models import Company
from apps.common.models import (
    LocationStateCode,
    LocationCountryCode
)


class JobListingStateMachineTests(TestCase):

    def create_job_listing_with_status(
        self,
        status=JobListingState.DRAFT,
        date_to_publish=datetime.now(),
        date_to_expire=date.today(),
        closed_date=datetime.now()
    ):
        with mixer.ctx(commit=False):
            return mixer.blend(
                JobListing,
                company=Company.objects.get(id=1),
                country=LocationCountryCode.objects.get(id=1),
                state=LocationStateCode.objects.get(id=1),
                date_to_publish=date_to_publish,
                date_to_expire=date_to_expire,
                closed_date=closed_date,
                status=status
            )

    @classmethod
    def setUpTestData(cls):
        country = mixer.blend(LocationCountryCode)
        state = mixer.blend(LocationStateCode, country_id=country.id)
        mixer.blend(Company, state_id=state.id, country_id=country.id)

    def test_can_pre_publish(self):
        """
        This test asserts that a JobListing can be transitioned to the 
        PREPUBLISH state if it is currently in the DRAFT state
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.DRAFT
        )

        self.assertTrue(can_proceed(job_listing.pre_publish))

    def test_can_publish_job_listing_if_date_to_publish_now_or_in_past(self):
        """
        This test asserts that a JobListing can be transitioned to the
        PUBLISHED state if it is currently in the PREPUBLISH state, and
        the date_to_publish date is in the past or present
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.PREPUBLISH,
            date_to_publish=datetime.now()
        )

        self.assertTrue(can_proceed(job_listing.publish))

    def test_cannot_publish_job_listing_if_date_to_publish_in_future(self):
        """
        This test asserts that a JobListing cannot be transitioned to the
        PUBLISHED state if it is currently in the PREPUBLISH state, but the
        date_to_publish date is in the future
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.PREPUBLISH,
            date_to_publish=(datetime.now() + timedelta(days=1))
        )

        self.assertFalse(can_proceed(job_listing.publish))

    def test_job_listing_can_expire_if_past_expiry_date(self):
        """
        This test asserts that a JobListing can be transitioned to the
        EXPIRED state if it is currently in the PUBLISHED state, and the
        date_to_expire date is in the past or present
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.PUBLISHED,
            date_to_expire=date.today()
        )

        self.assertTrue(can_proceed(job_listing.expire))

    def test_job_listing_cannot_expire_if_before_expiry_date(self):
        """
        This test asserts that a JobListing cannot be transitioned to the
        EXPIRED state if it is currently in the PUBLISHED state, but the
        date_to_expire date is in the future
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.PUBLISHED,
            date_to_expire=(date.today() + timedelta(days=1))
        )

        self.assertFalse(can_proceed(job_listing.expire))

    def test_published_job_listing_can_close(self):
        """
        This test asserts that a JobListing can be transitioned to the
        CLOSED state if it is currently in the PUBLISHED state
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.PUBLISHED
        )

        self.assertTrue(can_proceed(job_listing.close))

    def test_expired_job_listing_can_be_archived_after_one_month(self):
        """
        This test asserts that a JobListing can be transitioned to the
        ARCHIVED state if it is currently in the EXPIRED state, and the
        closed_date date is at least 30 days before the current date
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.EXPIRED,
            closed_date=(datetime.now() - timedelta(days=30))
        )

        self.assertTrue(can_proceed(job_listing.archive))

    def test_expired_job_listing_cannot_be_archived_before_one_month(self):
        """
        This test asserts that a JobListing cannot be transitioned to the
        ARCHIVED state if it is currently in the EXPIRED state, but the
        closed_date date is less than 30 days before the current date
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.EXPIRED,
            closed_date=datetime.now()
        )

        self.assertFalse(can_proceed(job_listing.archive))

    def test_closed_job_listing_can_be_archived_after_one_month(self):
        """
        This test asserts that a JobListing can be transitioned to the
        ARCHIVED state if it is currently in the CLOSED state, and the
        closed_date date is at least 30 days before the current date
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.CLOSED,
            closed_date=(datetime.now() - timedelta(days=30))
        )

        self.assertTrue(can_proceed(job_listing.archive))

    def test_closed_job_listing_cannot_be_archived_before_one_month(self):
        """
        This test asserts that a JobListing cannot be transitioned to the
        ARCHIVED state if it is currently in the CLOSED state, but the
        closed_date date is less than 30 days before the current date
        """

        job_listing = self.create_job_listing_with_status(
            status=JobListingState.CLOSED,
            closed_date=datetime.now()
        )

        self.assertFalse(can_proceed(job_listing.archive))
