from rest_framework.serializers import ModelSerializer
from Repository import Comment


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        models = Comment
        fields = ["user_id", "comment"]
