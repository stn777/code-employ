from django.db import models


class Applicant(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.PROTECT
    )
    location = models.ForeignKey(
        'common.Location', 
        on_delete=models.PROTECT
    )
    date_of_birth = models.DateField(null=False)
    website_url = models.TextField(null=True)
    github_url = models.TextField(null=True)


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