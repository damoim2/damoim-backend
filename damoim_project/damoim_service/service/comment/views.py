from rest_framework import status, permissions, viewsets

from damoim_service.deserializer.CommentAPI.create_comment_deserializer import (
    CreateCommentDeserializer,
)
from libs.Response import Response
from damoim_service.library.CommentAPI.create_comment import post_comment_to_post


class CommentAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create_comment(self, request, post_id):
        deserializer = CreateCommentDeserializer(request.data)
        post_comment_to_post(
            command=deserializer.create(), post_id=post_id, user_id=request.user.uuids
        )
        return Response(status=status.HTTP_201_CREATED, flag=True)
