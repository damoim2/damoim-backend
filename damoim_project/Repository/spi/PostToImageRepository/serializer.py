from rest_framework.serializers import ModelSerializer

from damoim_service.models import PostToImage


class CreatePostToImageSerializer(ModelSerializer):
    class Meta:
        models = PostToImage
        fields = ["post_id", "image_url"]