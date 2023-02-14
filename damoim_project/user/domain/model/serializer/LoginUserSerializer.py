from rest_framework.serializers import Serializer, CharField, ValidationError
from django.contrib.auth import authenticate
class LoginUserSerializer(Serializer):
    username = CharField()
    password = CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError(
            "Unable to log in with provided credentials.")

