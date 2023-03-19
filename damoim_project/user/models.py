from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from libs.base.models import SoftDeleteModel


# Create your models here

class KakaoAuth(SoftDeleteModel):
    kakao_id = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "kakao_auth"

class User(SoftDeleteModel):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, auto_created=True)
    gender = models.BooleanField(default=False)
    is_allow_data_share = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"
class SocialToUser(models.Model):
    social_id = models.CharField(primary_key=True)
    user_id = models.ForeignKey(User, models.CASCADE, db_column='user_id')
    class Meta:
        db_table = "social_to_user"

class Group(models.Model):
    group_id = models.BigAutoField(primary_key=True)
    group_name = models.CharField(unique=True, null=False, max_length=255)
    group_thumbnail = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "group"

class GroupToUser(models.Model):
    index = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id')
    group_id = models.ForeignKey(Group, models.DO_NOTHING, db_column='group_id')
    class Meta:
        db_table = "group_to_user"