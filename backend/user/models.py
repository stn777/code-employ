from django.db import models


class User(models.Model):
    email = models.TextField(null=False, unique=True, max_length=255)
    password_hash = models.TextField(null=False, max_length=255)
    first_name = models.TextField(null=False, max_length=255)
    surname = models.TextField(null=False, max_length=255)
    account_type = models.TextField(null=False, max_length=100)
    date_of_birth = models.DateField(null=False)
    date_inactive = models.DateTimeField(null=True, default=None)
    created_date = models.DateTimeField(null=False, auto_now_add=True)

