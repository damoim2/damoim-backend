from rest_framework import serializers

from damoim_service.command.Calendar import CreateUserScheduleCommand
from libs.Exception import ClientRequestValidationError
from datetime import datetime


class CreateUserScheduleDeserializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    from_date = serializers.CharField()
    to_date = serializers.CharField()
    time = serializers.CharField()
    title = serializers.CharField()
    address = serializers.CharField()
    memo = serializers.CharField()
    icon_id = serializers.IntegerField()
    color = serializers.CharField()
    is_day_on = serializers.BooleanField()

    def create(self):
        if self.is_valid():
            from_date = datetime.strptime(self.validated_data["from_date"], "%Y-%m-%d")
            to_date = datetime.strptime(self.validated_data["to_date"], "%Y-%m-%d")
            time = datetime.strptime("%H%M%s")

            return CreateUserScheduleCommand(
                user_id=self.validated_data["user_id"],
                from_date=from_date,
                to_date=to_date,
                time=time,
                title=self.validated_data["title"],
                address=self.validated_data["address"],
                memo=self.validated_data["memo"],
                icon_id=self.validated_data["icon_id"],
                color=self.validated_data["color"],
                is_day_on=self.validated_data["is_day_on"],
            )
        else:
            raise ClientRequestValidationError()
