from rest_framework import status

from damoim_service.deserializer.GroupAPI.create_deserializer import CreateDeserializer
from damoim_service.deserializer.GroupAPI.map_user_group_deserializer import (
    MapUserGroupDeserializer,
)
from damoim_service.serializer.GroupAPI import GetGroupListSerializer
from damoim_service.serializer.GroupAPI.get_group_member_list_serializer import (
    GetGroupMemberListSerializer,
)

create_group_swagger = {
    "tags": ["Group"],
    "summary": "Create",
    "request": CreateDeserializer,
    "responses": {status.HTTP_201_CREATED: None},
}
get_group_list_swagger = {
    "tags": ["Group"],
    "summary": "Get List",
    "responses": {status.HTTP_200_OK: GetGroupListSerializer},
}
get_group_memeber_list_swagger = {
    "tags": ["Group"],
    "summary": "Get Member List",
    "responses": {status.HTTP_200_OK: GetGroupMemberListSerializer},
}
map_user_group_swagger = {
    "tags": ["Group"],
    "summary": "Mapping User To Group",
    "request": MapUserGroupDeserializer,
    "responses": {status.HTTP_200_OK: None},
}
