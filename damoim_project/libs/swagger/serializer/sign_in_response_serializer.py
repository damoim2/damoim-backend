from rest_framework import serializers


class SignInResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
