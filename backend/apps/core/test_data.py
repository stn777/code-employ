from apps.job_listing.models import (
    JobListing, JobListingLanguage,
    JobListingTag
)
from apps.job_listing.enums import (
    JobPositionType, JobListingState, SalaryFrequency
)
from apps.common.models import (
    LocationCountryCode, LocationStateCode,
    ProgrammingLanguage, Tag
)
from apps.job_listing_response.models import (
    JobListingResponse,
    JobListingResponseDocument,
    JobListingResponseOutcome
)
from apps.company.models import Company, UserCompany
from apps.applicant.models import Applicant, ApplicantLanguage
from apps.user.models import User
from .providers.faker.job_title import Provider as job_title_provider
from faker import Faker


fake = Faker()
fake.add_provider(job_title_provider)
COMPANY_COUNT = 3
JOB_LISTING_COUNT = 5


def reset_data():
    clear_data()
    country = _create_country_code()
    state = _create_state_code(country)
    _create_tags()
    _create_programming_languages()

    for i in range(COMPANY_COUNT):
        company = _create_company(country, state)
        for j in range(JOB_LISTING_COUNT):
            job_listing = _create_job_listing(company)
            _create_job_listing_languages(job_listing)
            _create_job_listing_tags(job_listing)


def clear_data():
    JobListingTag.objects.all().delete()
    JobListingLanguage.objects.all().delete()
    JobListingResponseOutcome.objects.all().delete()
    JobListingResponseDocument.objects.all().delete()
    JobListingResponse.objects.all().delete()
    JobListing.objects.all().delete()

    Company.objects.all().delete()
    ApplicantLanguage.objects.all().delete()
    Applicant.objects.all().delete()
    User.objects.all().delete()

    ProgrammingLanguage.objects.all().delete()
    LocationCountryCode.objects.all().delete()
    LocationStateCode.objects.all().delete()
    Tag.objects.all().delete()


def _create_country_code():
    country = LocationCountryCode(
        name="Australia",
        code="AU"
    )
    country.save()
    return country


def _create_state_code(country):
    state = LocationStateCode(
        country=country,
        name="Victoria",
        code="VIC"
    )
    state.save()
    return state


def _create_programming_languages():
    languages = ['Python', 'Javascript']
    for language in languages:
        new_language = ProgrammingLanguage(name=language)
        new_language.save()


def _create_tags():
    tags = ['Django', 'React']
    for tag in tags:
        new_tag = Tag(title=tag)
        new_tag.save()


def _create_company(country, state):
    company = Company(
        legal_name=fake.company(),
        email=fake.company_email(),
        website_url=fake.domain_name(),
        city="Melbourne",
        country=country,
        state=state,
        post_code="3000"
    )
    company.save()
    return company


def _create_job_listing(company):
    job_listing = JobListing(
        company=company,
        job_title=fake.job_title(),
        description=fake.text(max_nb_chars=200),
        position_type=JobPositionType.FULLTIME,
        salary=round(fake.random_int(60000, 180000), -3),
        salary_frequency=SalaryFrequency.PERYEAR,
        city=company.city,
        country=company.country,
        state=company.state,
        post_code="3000",
        status=JobListingState.PUBLISHED
    )
    job_listing.save()
    return job_listing


def _create_job_listing_languages(job_listing):
    languages = ProgrammingLanguage.objects.all()
    for language in languages:
        job_listing_language = JobListingLanguage(
            job_listing=job_listing,
            language=language
        )
        job_listing_language.save()


def _create_job_listing_tags(job_listing):
    tags = Tag.objects.all()
    for tag in tags:
        job_listing_tag = JobListingTag(
            job_listing=job_listing,
            tag=tag
        )
        job_listing_tag.save()
