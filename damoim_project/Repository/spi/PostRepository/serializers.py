from rest_framework.serializers import ModelSerializer

from damoim_service.models import Post


class CreatePostSerializer(ModelSerializer):
    class Meta:
        models = Post
        fields = ["user_id", "contents", "title", "group_id"]
