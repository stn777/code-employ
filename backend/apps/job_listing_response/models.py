from django.db import models
from apps.applicant.models import Applicant


class JobListingResponse(models.Model):
    applicant = models.ForeignKey(
        'applicant.Applicant',
        on_delete=models.PROTECT
    )
    job_listing = models.ForeignKey(
        'job_listing.JobListing',
        on_delete=models.PROTECT
    )
    status = models.TextField(null=False, max_length=100)
    created_date = models.DateTimeField(null=False, auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now=True)


class JobListingResponseOutcome(models.Model):
    job_listing_response = models.ForeignKey(
        JobListingResponse,
        on_delete=models.PROTECT
    )
    outcome = models.TextField(null=False, max_length=100)
    outcome_comments = models.TextField(null=False)
    outcome_date = models.DateTimeField(null=False, auto_now_add=True)


class JobListingResponseDocument(models.Model):
    job_listing_response = models.ForeignKey(
        JobListingResponse,
        on_delete=models.PROTECT
    )
    file = models.ForeignKey(
        'common.File',
        on_delete=models.CASCADE
    )
    filename = models.TextField(null=False)
    file_size = models.IntegerField(null=False)
