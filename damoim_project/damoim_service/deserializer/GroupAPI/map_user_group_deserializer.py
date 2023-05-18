from rest_framework import serializers

from damoim_service.command.GroupToUser import CreateGroupToUserCommand
from libs.Exception import ClientRequestValidationError


class MapUserGroupDeserializer(serializers.Serializer):
    group_id = serializers.IntegerField()

    def create(self, user_id: int):
        if self.is_valid():
            return CreateGroupToUserCommand(
                user_id=user_id, group_id=self.validated_data["group_id"]
            )
        else:
            raise ClientRequestValidationError()
