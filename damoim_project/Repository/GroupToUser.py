from .User import User
from .Group import Group
from .SoftDeleteModel import SoftDeleteModel
from django.db import models


class GroupToUser(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, db_column="fk_user_id", on_delete=models.DO_NOTHING, null=False
    )
    group_id = models.ForeignKey(
        Group, db_column="fk_group_id", on_delete=models.CASCADE, null=False
    )
    created_at = models.DateTimeField(auto_now=True)
