from rest_framework import serializers

from damoim_service.command.Post import CreatePostCommand
from damoim_service.models import User
from libs.Exception import ClientRequestValidationError


class CreatePostDeserializer(serializers.Serializer):
    title = serializers.CharField()
    contents = serializers.CharField()
    group_id = serializers.IntegerField()

    def create(self, user: User, images: list):
        if self.is_valid():
            return CreatePostCommand(
                user_id=user,
                title=self.validated_data["title"],
                contents=self.validated_data["contents"],
                group_id_id=self.validated_data["group_id"],
                image_contents=images,
            )
        else:
            raise ClientRequestValidationError()


"""
form-data
"data" : "{title: "asd ",contents:  "asd",group_id : 1}",
"images" : [images] 
"""
