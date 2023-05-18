from rest_framework.viewsets import ModelViewSet


from damoim_service.library.GroupAPI.create_post import create_post
from damoim_service.deserializer.PostAPI.create_post_deserializer import (
    CreatePostDeserializer,
)
from libs.Response import Response
from rest_framework import status, permissions


class PostAPI(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_list(self, request):
        return Response(status=status.HTTP_200_OK)

    def post_post(self, request):
        deserializer = CreatePostDeserializer(request.data)
        post_command = deserializer.create(user=request.user)
        post, post_image = create_post(command=post_command)

        return Response(status=status.HTTP_201_CREATED)
