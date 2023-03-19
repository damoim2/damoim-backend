from user.models import User, Group
from libs.base.models import SoftDeleteModel
from django.db import models

# Create your models here.
class Post(SoftDeleteModel):
    post_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING, db_column="user_id")
    group_id = models.ForeignKey(Group, models.DO_NOTHING, db_column="group_id")
    contents = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Comment(SoftDeleteModel):
    reply_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING, db_column="user_id")
    post_id = models.ForeignKey(Post, models.DO_NOTHING, db_column="post_id")
    text = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class PostToPhoto(models.Model):
    index = models.BigAutoField(primary_key=True)
    photo = models.TextField(null=False)
    user_id = models.ForeignKey(User, models.DO_NOTHING, db_column="user_id")
    post_id = models.ForeignKey(Post, models.DO_NOTHING, db_column="post_id")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

