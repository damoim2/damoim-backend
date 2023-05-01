from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Repository.spi.Post.serializers import CreatePostSerializer
from Repository.spi.PostToImage.serializer import CreatePostToImageSerializer
from libs import S3


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def create(self, request):
        s3_uploader = S3.awsS3boto3()
        form = {
            "user_id": request.user,
            "title": request.data.get("title"),
            "contents": request.data.get("contents"),
            "group_id": request.user.group_set,
        }
        serializer = CreatePostSerializer(data=form)
        if serializer.is_valid():
            post = serializer.save()
            image = request.FILE
            url = s3_uploader.upload_file_s3(
                file=image,
                filename=str(post.index) + "_image",
                path=str(post.index),
                bucket_type="post",
            )
            form = {"post_id": post.index, "image_url": url}
            serializer = CreatePostToImageSerializer(data=form)
            if serializer.is_valid():
                serializer.save()
        return Response(status=status.HTTP_201_CREATED)


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
            },
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
            },
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
            },
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
