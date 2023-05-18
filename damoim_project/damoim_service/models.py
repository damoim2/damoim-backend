from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    # 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(deletedat__isnull=True)


class SoftDeleteModel(models.Model):
    # Field name made lowercase.
    deletedat = models.DateTimeField(db_column="deleted_at", blank=True, null=True)

    class Meta:
        abstract = True  # 상속 할수 있게

    objects = SoftDeleteManager()  # 커스텀 매니저
    objects_all = models.Manager()  # 매니저

    def delete(self, using=None, keep_parents=False):
        self.deletedat = timezone.now()
        self.save(update_fields=["deletedat"])

    def hard_delete(self):
        try:
            super(SoftDeleteModel, self).delete()
        except Exception as e:
            pass

    def restore(self):  # 삭제된 레코드를 복구한다.
        self.deletedat = None
        self.save(update_fields=["deletedat"])


class User(AbstractUser):
    uuids = models.TextField(max_length=500, null=False)
    name = models.CharField(max_length=100, null=False)
    thumbnail = models.CharField(max_length=255, null=True)


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


class GroupToUser(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, db_column="fk_user_id", on_delete=models.DO_NOTHING, null=False
    )
    group_id = models.ForeignKey(
        Group, db_column="fk_group_id", on_delete=models.CASCADE, null=False
    )
    created_at = models.DateTimeField(auto_now=True)


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


class Comment(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, db_column="fk_user_id", null=False, on_delete=models.DO_NOTHING
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class CommentToPost(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    comment_id = models.ForeignKey(
        Comment, db_column="fk_comment_id", on_delete=models.CASCADE
    )
    post_id = models.ForeignKey(Post, db_column="fk_post_id", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, db_column="fk_user_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ConnectToSocial(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    # Social 연동으로 들어올 uuid
    uuid = models.IntegerField(null=False)
    # 1 : kakao, 2 : Apple, 3 : Google, 4 : FaceBook
    type = models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class LikeToPost(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(
        Post, db_column="fk_post_id", on_delete=models.DO_NOTHING
    )
    user_id = models.ForeignKey(
        User, db_column="fk_user_id", on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now=True)


class PostToImage(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(
        Post, on_delete=models.DO_NOTHING, null=False, db_column="fk_post_id"
    )
    image_url = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
