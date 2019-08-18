from django.conf import settings
from celery import shared_task
from code_employ.celery import TransactionTask
from .business.selectors import JobListingSelector


@shared_task(base=TransactionTask, bind=True, max_retries=settings.CELERY_MAX_RETRIES)
def publish_job_listings(self):
    job_listings = JobListingSelector.get_job_listings_ready_for_publish()

    for job_listing in job_listings:
        if job_listing.can_proceed(job_listing.publish):
            job_listing.publish()
            job_listing.save()


@shared_task(base=TransactionTask, bind=True, max_retries=settings.CELERY_MAX_RETRIES)
def expire_published_job_listings(self):
    job_listings = JobListingSelector.get_job_listings_ready_for_expiry()

    for job_listing in job_listings:
        if job_listing.can_proceed(job_listing.expire):
            job_listing.expire()
            job_listing.save()


@shared_task(base=TransactionTask, bind=True, max_retries=settings.CELERY_MAX_RETRIES)
def archive_closed_and_expired_job_listings(self):
    job_listings = JobListingSelector.get_job_listings_ready_for_archive()

    for job_listing in job_listings:
        if job_listing.can_proceed(job_listing.archive):
            job_listing.archive()
            job_listing.save()
