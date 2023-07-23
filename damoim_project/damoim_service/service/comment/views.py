from rest_framework import status, permissions, viewsets

from damoim_service.deserializer.CommentAPI.create_comment_deserializer import (
    CreateCommentDeserializer,
)
from damoim_service.library.CommentAPI.delete_comment import delete
from libs.Response import Response
from damoim_service.library.CommentAPI.create_comment import post_comment_to_post


class CommentAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create_comment(self, request, post_id):
        deserializer = CreateCommentDeserializer(data=request.data)
        post_comment_to_post(
            command=deserializer.create(user_id=request.user.id), post_id=post_id
        )
        return Response(status=status.HTTP_201_CREATED, flag=True)

    def delete_comment(self, request, post_id):
        delete(post_id=post_id, user_id=request.user.id)
        return Response(status=status.HTTP_200_OK, flat=True)
