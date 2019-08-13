from django.db import models


class Applicant(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.PROTECT
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
    website_url = models.TextField(null=True)
    github_url = models.TextField(null=True)
    languages = models.ManyToManyField(
        'common.ProgrammingLanguage',
        through='ApplicantLanguage'
    )


class ApplicantLanguage(models.Model):
    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.PROTECT
    )
    language = models.ForeignKey(
        'common.ProgrammingLanguage',
        on_delete=models.CASCADE
    )
    years_of_experience = models.IntegerField(null=False)