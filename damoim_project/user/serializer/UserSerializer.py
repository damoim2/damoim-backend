from rest_framework.serializers import ModelSerializer
from user.models import User, KakaoAuth, SocialToUser


class UserCreateSerializer(ModelSerializer):
    class Meta:
        models = User
        field = "__all__"


class KakaoAuthSerializer(ModelSerializer):
    class Meta:
        models = KakaoAuth
        field = "__all__"
