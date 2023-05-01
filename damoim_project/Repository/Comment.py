from .SoftDeleteModel import SoftDeleteModel
from .User import User
from django.db import models


class Comment(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, db_column="fk_user_id", null=False, on_delete=models.DO_NOTHING
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
