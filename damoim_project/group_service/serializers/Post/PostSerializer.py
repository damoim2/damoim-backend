from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    IntegerField,
)
from group_service.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        models = Post
        fields = "__all__"


class PostGETSerializer(PostSerializer):
    class Meta:
        models = Post
        exclude = ["deletedat", "updatedat", "index"]


class PostCREATESerializer(PostSerializer):
    class Meta:
        models = Post
        exclude = ["deletedat"]


class PostUPDATESerializer(PostSerializer):
    class Meta:
        models = Post
        exclude = ["deletedat"]


class PostListSerializer(Serializer):
    name = CharField(max_length=50, allow_null=False, allow_blank=False)
    user_id = CharField(max_length=50, allow_null=False, allow_blank=False)
    contents = CharField(max_length=None, allow_null=False, allow_blank=False)
    date = CharField(max_length=50, allow_null=False, allow_blank=False)
    like_count = IntegerField(allow_null=False)
    comment_count = IntegerField(allow_null=False)
    post_id = IntegerField(allow_null=False)
