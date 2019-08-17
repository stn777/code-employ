from django.conf import settings
from celery import shared_task
from code_employ.celery import TransactionTask
from .enums import JobListingState
from .business.selectors import JobListingSelector


@shared_task(base=TransactionTask, bind=True, max_retries=settings.CELERY_MAX_RETRIES)
def publish_job_listings(self):
    job_listings = JobListingSelector.get_job_listings_by_status(JobListingState.PREPUBLISH)

    for job_listing in job_listings:
        if job_listing.can_proceed(job_listing.publish):
            job_listing.publish()
            job_listing.save()
