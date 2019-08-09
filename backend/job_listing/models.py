from django.db import models


class JobListing(models.Model):
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.PROTECT
    )
    job_title = models.TextField(null=False, max_length=255)
    description = models.TextField(null=False)
    location = models.ForeignKey(
        'common.Location',
        on_delete=models.PROTECT
    )
    position_type = models.TextField(null=False, max_length=100)
    contract_length = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    salary_frequency = models.TextField(null=True, max_length=100)
    expiry_date = models.DateTimeField(null=True, default=None)
    posted_date = models.DateTimeField(null=False, auto_now_add=True)
    modified_date = models.DateTimeField(null=True, auto_now=True)


class JobListingLanguage(models.Model):
    job_listing = models.ForeignKey(
        JobListing,
        on_delete=models.CASCADE
    )
    language = models.ForeignKey(
        'common.ProgrammingLanguage',
        on_delete=models.CASCADE
    )
    

class JobListingRequiredDocument(models.Model):
    job_listing = models.ForeignKey(
        JobListing,
        on_delete=models.CASCADE
    )
    title = models.TextField(null=False)
    description = models.TextField(null=False)


class JobListingTag(models.Model):
    job_listing = models.ForeignKey(
        JobListing,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        'common.Tag',
        on_delete=models.PROTECT
    )


class JobListingResponse(models.Model):
    applicant = models.ForeignKey(
        'applicant.Applicant',
        on_delete=models.PROTECT
    )
    job_listing = models.ForeignKey(
        JobListing,
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