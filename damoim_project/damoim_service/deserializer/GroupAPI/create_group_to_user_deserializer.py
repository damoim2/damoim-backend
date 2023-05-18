from django.utils import timezone
from rest_framework import serializers

from damoim_service.command.GroupToUser import CreateGroupToUserCommand
from libs.Exception import ClientRequestValidationError


class CreateGroupToUserDeserializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def create(self, group_id: int, today: timezone):
        if self.is_valid():
            return CreateGroupToUserCommand(
                user_id=self.validated_data["user_id"], group_id=group_id
            )
        else:
            raise ClientRequestValidationError()
