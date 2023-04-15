import permission as permission
from rest_framework import viewsets, status
from rest_framework import permissions

from group_service.models import Post
from libs.base.response import ReturnResponse as Response
from group_service.serializers.Post.PostDeSerializer import PostFormDeSerialier
from group_service.serializers.Post.PostSerializer import (
    PostCREATESerializer,
    PostGETSerializer,
)
from libs.exception.exceptions import PostCreateError, PostGetError
from user.models import Group


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user_id = request.user.user_id
        group_id = Group.objects.get(grouptouser__user_id_id=user_id)
        image_list = request.FILES["Photos"]
        # upload to s3
        # Todo make "upload S3 Function"
        requested_data = request.data
        requested_data = requested_data.update({"group_id": group_id})
        deserializer_object = PostFormDeSerialier(requested_data)
        valid_form = deserializer_object.create(user_id=user_id, group_id=group_id)
        create_serializer = PostCREATESerializer(data=valid_form)
        if create_serializer.is_valid():
            create_serializer.create()
            return Response(
                flag=True,
                code="SERV0000",
                data=create_serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            raise PostCreateError()

    def get(self, request):
        post_id = request.parser_context.get("pid")
        query = Post.objects.get(post_id=post_id)
        serializer = PostGETSerializer(query)
        if serializer.is_valid():
            return Response(
                flag=True,
                code="SERV0000",
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        else:
            raise PostGetError()

    def list(self, request):
        user_id = request.user.user_id_id

    def delete(self, request):
        post_id = request.parser_context.get("pid")
        query = Post.objects.get(post_id=post_id)
        query.delete()
        return

    def update(self, request):
        # update 나중에 정해지고 나서 진행
        # Todo partial_update dev
        return


"""
# 글목록 불러오기
{
    "is_success": flag,
    "code": code,
    "data": {
        "post_list" :[
            {
                "user" : {
                    "name": "홍길동",
                    "user_id" "12",
                    "user_thumbnail" : "BASE64CODE"
                },
                "post" : {
                    "contents" : "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                    "date" : "20230303",
                    "like_count" : 0,
                    "comment_count" : 0,
                    "thumbnail" : "Base64 Code"
                }
                "is_like" : True, # True : 좋아요, False : 싫어요
                "is_editable" : True # True : 수정 가능, False : 수정 불가
            }
        ]
    }
}
"""

"""
# 글 디테일 불러오기
{
    "is_success": True,
    "code": code,
    "data": {
        "post":
            {
                "user" : {
                    "name": "홍길동",
                    "user_id" "12",
                    "user_thumbnail" : "BASE64CODE",
                },
                "post" : {
                    "contents" : "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                    "date" : "20230303",
                    "like_count" : 0,
                    "thumbnail_list" : ["Base64 Code"]
                }
            }
        
        "reply_list" :[
            {
                "user" : {
                    "name": "홍길동",
                    "user_id" "12",
                    "user_thumbnail" : "BASE64CODE",
                },
                "comment" : {
                    "contents" : "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                    "date" : "20230303",
                }
            }
        ]
    }
} 

"""


# 댓글작성하기
# 좋아요 하기
# 사진 첨부하기
