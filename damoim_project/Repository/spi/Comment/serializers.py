from rest_framework.serializers import ModelSerializer

from damoim_service.models import Comment


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        models = Comment
        fields = ["user_id", "comment"]
