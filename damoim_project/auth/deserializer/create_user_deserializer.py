from rest_framework import serializers

from auth.command.create_user_command import CreateUserCommand
from libs.Exception import ClientRequestValidationError


class CreateUserDeserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    uuids = serializers.IntegerField()
    name = serializers.CharField()

    def create(self) -> CreateUserCommand:
        if self.is_valid():
            return CreateUserCommand(**self.validated_data)
        else:
            raise ClientRequestValidationError()
