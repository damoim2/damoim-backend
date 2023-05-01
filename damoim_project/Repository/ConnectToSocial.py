from django.db import models
from .SoftDeleteModel import SoftDeleteModel


class ConnectToSocial(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    # Social 연동으로 들어올 uuid
    uuid = models.IntegerField(null=False)
    # 1 : kakao, 2 : Apple, 3 : Google, 4 : FaceBook
    type = models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
