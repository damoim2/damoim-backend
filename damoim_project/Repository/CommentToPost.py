from .SoftDeleteModel import SoftDeleteModel
from .User import User
from .Post import Post
from .Comment import Comment
from django.db import models


class CommentToPost(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    comment_id = models.ForeignKey(
        Comment, db_column="fk_comment_id", on_delete=models.CASCADE
    )
    post_id = models.ForeignKey(Post, db_column="fk_post_id", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, db_column="fk_user_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
