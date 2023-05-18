from rest_framework import serializers


class GetGroupListSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    name = serializers.CharField()
    thumbnail = serializers.CharField()
