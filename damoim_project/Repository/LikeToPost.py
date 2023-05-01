from .SoftDeleteModel import SoftDeleteModel
from .Post import Post
from .User import User
from django.db import models


class LikeToPost(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(
        Post, db_column="fk_post_id", on_delete=models.DO_NOTHING
    )
    user_id = models.ForeignKey(
        User, db_column="fk_user_id", on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now=True)
