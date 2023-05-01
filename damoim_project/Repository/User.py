from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uuids = models.TextField(max_length=500, null=False)
    name = models.CharField(max_length=100, null=False)
    thumbnail = models.CharField(max_length=255, null=True)
