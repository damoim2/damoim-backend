from rest_framework.viewsets import ModelViewSet

from damoim_service.command.GroupAPI import PostLikeCommand
from damoim_service.library.GroupAPI.create_like_to_post import create_like_to_post
from damoim_service.library.GroupAPI.create_post import create_post
from damoim_service.deserializer.PostAPI.create_post_deserializer import (
    CreatePostDeserializer,
)
from libs.Response import Response
from rest_framework import status, permissions
import json


class PostAPI(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_list(self, request):
        return Response(status=status.HTTP_200_OK)

    def post_post(self, request):
        data = request.POST["data"]
        data = json.loads(data)
        image = request.FILES["images"]
        deserializer = CreatePostDeserializer(data=data)
        post_command = deserializer.create(user=request.user.id, image=image)
        create_post(command=post_command)
        return Response(status=status.HTTP_201_CREATED)

    def post_like(self, request, post_id: int):
        count = create_like_to_post(
            PostLikeCommand(user_id=request.user.id, post_id=post_id)
        )
        return Response(data=count, status=status.HTTP_201_CREATED)
