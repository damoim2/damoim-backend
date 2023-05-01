from .SoftDeleteModel import SoftDeleteModel
from .Post import Post

from django.db import models


class PostToImage(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(
        Post, on_delete=models.DO_NOTHING, null=False, db_column="fk_post_id"
    )
    image_url = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
