from django.core.files import File
from rest_framework import serializers

from damoim_service.command.GroupAPI import CreateGroup
from libs.Exception import ClientRequestValidationError


class CreateDeserializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, user_id: int, thumbnail: File):
        if self.is_valid():
            return CreateGroup(
                user_id=user_id, name=self.validated_data["name"], files=thumbnail
            )
        else:
            raise ClientRequestValidationError()
