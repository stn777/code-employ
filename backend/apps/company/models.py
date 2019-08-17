from django.db import models


class Company(models.Model):
    legal_name = models.TextField(null=False, max_length=255)
    email = models.TextField(null=False, max_length=255)
    website_url = models.TextField(null=True)
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
    date_inactive = models.DateTimeField(null=True, default=None)
    created_date = models.DateTimeField(null=False, auto_now_add=True)


class UserCompany(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.PROTECT
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT
    )