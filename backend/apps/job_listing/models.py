from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, date, timedelta
from django_fsm import FSMIntegerField, transition
from enumchoicefield import EnumChoiceField
from apps.core.managers import ModelManager
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

    def can_publish(self):
        return self.date_to_publish <= datetime.now()

    def can_expire(self):
        return self.date_to_expire <= date.today()

    def can_archive(self):
        return self.closed_date <= (datetime.now() - timedelta(days=30))

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
        target=JobListingState.PUBLISHED,
        conditions=[can_publish]
    )
    def publish(self):
        pass

    @transition(
        field=status,
        source=JobListingState.PUBLISHED,
        target=JobListingState.EXPIRED,
        conditions=[can_expire]
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
        conditions=[can_archive]
    )
    def archive(self):
        pass


class JobListingList(models.Model):
    '''Postgres database view'''
    id = models.BigIntegerField(primary_key=True)
    company_name = models.TextField()
    job_title = models.TextField()
    description = models.TextField()
    position_type = EnumChoiceField(
        enum_class=JobPositionType
    )
    contract_length = models.IntegerField()
    salary = models.IntegerField()
    salary_frequency = EnumChoiceField(
        enum_class=SalaryFrequency
    )
    languages = ArrayField(models.TextField())
    city = models.TextField()
    state_name = models.TextField()
    country_name = models.TextField()
    post_code = models.TextField()
    tags = ArrayField(models.TextField())
    created_date = models.DateTimeField()
    objects = ModelManager()

    class Meta:
        managed = False
        db_table = 'job_listing_joblistinglistview'


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
