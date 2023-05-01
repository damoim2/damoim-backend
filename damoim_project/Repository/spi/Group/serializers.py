from rest_framework.serializers import ModelSerializer
from Repository import Group


class CreateGroupSerializer(ModelSerializer):
    class Meta:
        models = Group
        fields = ["name", "owner", "thumbnail"]
