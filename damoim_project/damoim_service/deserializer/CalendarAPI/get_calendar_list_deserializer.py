from rest_framework import serializers


class GetCalendarListDeserializer(serializers.Serializer):
    check_year = serializers.IntegerField(allow_null=False)
    check_month = serializers.IntegerField(allow_null=False)
    user_id = serializers.IntegerField(allow_null=False)

    def create(self):
        return
