from .SoftDeleteModel import SoftDeleteModel
from .User import User
from django.db import models


class Group(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    owner = models.ForeignKey(
        User,
        db_column="fk_user_id",
        help_text="그룹 소유주",
        on_delete=models.DO_NOTHING,
        null=False,
    )
    thumbnail = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
