from django.db import models
from .SoftDeleteModel import SoftDeleteModel
from .User import User
from .Group import Group


class Post(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_column="fk_user_id"
    )
    group_id = models.ForeignKey(
        Group, on_delete=models.DO_NOTHING, db_column="fk_group_id"
    )
    title = models.CharField(max_length=255, null=False)
    contents = models.TextField(null=True)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)
