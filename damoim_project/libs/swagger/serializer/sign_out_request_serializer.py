from rest_framework import serializers


class SignOutRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()
