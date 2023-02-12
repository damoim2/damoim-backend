from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "password", "uuids")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

