from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, auto_created=True
    )

    class Meta:
        db_table = "User"
