from drf_spectacular.utils import extend_schema

from damoim_service.deserializer.GroupAPI.create_deserializer import CreateDeserializer
from damoim_service.deserializer.GroupAPI.map_user_group_deserializer import (
    MapUserGroupDeserializer,
)
from damoim_service.library.GroupAPI.map_user_to_group import map_user_to_group
from damoim_service.library.GroupAPI.create_group import create_group
from damoim_service.serializer.GroupAPI import GetGroupListSerializer
from damoim_service.serializer.GroupAPI.get_group_member_list_serializer import (
    GetGroupMemberListSerializer,
)
from libs.Response import Response
from rest_framework import viewsets, status, permissions
from damoim_service.library.GroupAPI import get_group_list, get_group_member_list
from libs.swagger.schema.group import (
    get_group_list_swagger,
    create_group_swagger,
    get_group_memeber_list_swagger,
    map_user_group_swagger,
)


class GroupAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(**get_group_list_swagger)
    def get_group_list(self, request):
        user_id = request.user.uuids
        serializer = GetGroupListSerializer(get_group_list(user_id=user_id), many=True)
        return Response(data=serializer.data, flag=True, status=status.HTTP_200_OK)

    @extend_schema(**get_group_memeber_list_swagger)
    def get_group_member_list(self, request, group_id):
        serializer = GetGroupMemberListSerializer(
            get_group_member_list(group_id=group_id), many=True
        )
        return Response(data=serializer.data, flag=True, status=status.HTTP_200_OK)

    @extend_schema(**create_group_swagger)
    def create(self, request):
        deserializer = CreateDeserializer(data=request.data)
        command = deserializer.create(
            user_id=request.user.uuids,
            thumbnail=request.FILES["thumbnail"]
            if "thumbnail" in request.FILES
            else None,
        )
        create_group(command)
        return Response(data={}, flag=True, status=status.HTTP_201_CREATED)

    @extend_schema(**map_user_group_swagger)
    def map_user_group(self, request):
        deserializer = MapUserGroupDeserializer(data=request.data)
        command = deserializer.create(user_id=request.user.uuids)
        map_user_to_group(command)
        return Response(data={}, flag=True, status=status.HTTP_200_OK)
