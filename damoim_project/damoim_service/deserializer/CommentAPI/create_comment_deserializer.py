from rest_framework import serializers

from damoim_service.command.Comment import CreateCommentCommand
from libs.Exception import ClientRequestValidationError


class CreateCommentDeserializer(serializers.Serializer):
    comment = serializers.CharField()

    def create(self, user_id):
        if self.is_valid():
            return CreateCommentCommand(
                comment=self.validated_data["comment"], user_id=user_id
            )
        else:
            raise ClientRequestValidationError()
