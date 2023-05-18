from rest_framework.serializers import ModelSerializer

from damoim_service.models import Group


class CreateGroupSerializer(ModelSerializer):
    class Meta:
        models = Group
        fields = ["name", "owner", "thumbnail"]
