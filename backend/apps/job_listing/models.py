from django.db import models
from django_fsm import FSMIntegerField, transition
from enumchoicefield import EnumChoiceField
from apps.common.managers import ModelManager
from .enums import JobPositionType, SalaryFrequency, JobListingState


class JobListing(models.Model):
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.PROTECT
    )
    job_title = models.TextField(null=False, max_length=255)
    description = models.TextField(null=False)
    position_type = EnumChoiceField(
        enum_class=JobPositionType,
        default=JobPositionType.FULLTIME
    )
    contract_length = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    salary_frequency = EnumChoiceField(
        enum_class=SalaryFrequency,
        default=SalaryFrequency.PERYEAR
    )
    languages = models.ManyToManyField(
        'common.ProgrammingLanguage',
        through='JobListingLanguage'
    )
    city = models.TextField(null=False, max_length=100)
    state = models.ForeignKey(
        'common.LocationStateCode',
        on_delete=models.PROTECT
    )
    country = models.ForeignKey(
        'common.LocationCountryCode',
        on_delete=models.PROTECT
    )
    post_code = models.TextField(null=False, max_length=10)
    tags = models.ManyToManyField(
        'common.Tag',
        through='JobListingTag'
    )
    status = FSMIntegerField(default=JobListingState.DRAFT)
    date_to_publish = models.DateTimeField(null=True)
    date_to_expire = models.DateField(null=True)
    closed_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(null=False, auto_now_add=True)
    modified_date = models.DateTimeField(null=True, auto_now=True)
    objects = ModelManager()

    @transition(
        field=status,
        source=JobListingState.DRAFT,
        target=JobListingState.PREPUBLISH
    )
    def pre_publish(self):
        pass

    @transition(
        field=status,
        source=JobListingState.PREPUBLISH,
        target=JobListingState.PUBLISHED
    )
    def publish(self):
        pass

    @transition(
        field=status,
        source=JobListingState.PUBLISHED,
        target=JobListingState.EXPIRED
    )
    def expire(self):
        pass

    @transition(
        field=status,
        source=JobListingState.PUBLISHED,
        target=JobListingState.CLOSED
    )
    def close(self):
        pass

    @transition(
        field=status,
        source=[JobListingState.EXPIRED, JobListingState.CLOSED],
        target=JobListingState.ARCHIVED,
    )
    def archive(self):
        pass


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