from rest_framework import serializers

from damoim_service.command.Group import CreateGroupCommand
from libs.Exception import ClientRequestValidationError


class CreateGroupDeserializer(serializers.Serializer):
    name = serializers.CharField()
    user_id = serializers.IntegerField()

    def create(self, thumbnail: str):
        if self.is_valid():
            return CreateGroupCommand(
                name=self.validated_data["name"],
                owner=self.validated_data["user_id"],
                thumbnail=thumbnail,
            )
        else:
            print(self.errors)
            raise ClientRequestValidationError()
