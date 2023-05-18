from rest_framework import serializers


class GetGroupMemberListSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    user_thumbnail = serializers.CharField()
