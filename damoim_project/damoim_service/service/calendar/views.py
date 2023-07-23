from rest_framework import viewsets, permissions, status

from damoim_service.command.Calendar import CreateUserScheduleCommand
from damoim_service.deserializer.CalendarAPI.create_user_calendar_schedule_deserializer import (
    CreateUserScheduleDeserializer,
)
from damoim_service.library.CalendarAPI.create_user_calendar import create_user_schedule
from libs.Response import Response
from damoim_service.command.Calendar import CreateGroupScheduleCommand
from damoim_service.deserializer.CalendarAPI.create_group_calendar_schedule_deserializer import (
    CreateGroupScheduleDeserializer,
)
from damoim_service.library.CalendarAPI.create_group_calendar import (
    create_group_schedule,
)


class CalendarAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create_user_schedule(self, request):
        command: CreateUserScheduleCommand = CreateUserScheduleDeserializer(
            request.data
        ).create()
        create_user_schedule(command)
        return Response(status=status.HTTP_201_CREATED, flag=True)

    def create_group_schedule(self, request):
        command: CreateGroupScheduleCommand = CreateGroupScheduleDeserializer(
            request.data
        ).create()
        create_group_schedule(command)
        return Response(status=status.HTTP_201_CREATED, flag=True)

    def get_list(self):
        command = ""
