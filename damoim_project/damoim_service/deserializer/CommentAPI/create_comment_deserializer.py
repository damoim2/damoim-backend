from rest_framework import serializers

from damoim_service.command.Comment import CreateCommentCommand
from libs.Exception import ClientRequestValidationError


class CreateCommentDeserializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    comment = serializers.CharField()

    def create(self):
        if self.is_valid():
            return CreateCommentCommand(**self.validated_data)
        else:
            raise ClientRequestValidationError()
