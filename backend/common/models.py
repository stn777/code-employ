from django.db import models


class Tag(models.Model):
    title = models.TextField(null=False, max_length=40)


class Location(models.Model):
    city = models.TextField(null=False, max_length=100)
    state = models.TextField(null=False, max_length=100)
    country = models.TextField(null=False, max_length=100)
    post_code = models.TextField(null=False, max_length=10)


class ProgrammingLanguage(models.Model):
    name = models.TextField(null=False, max_length=100)


class File(models.Model):
    file_bytes = models.BinaryField(null=False)
    created_date = models.DateTimeField(null=False, auto_now_add=True)
