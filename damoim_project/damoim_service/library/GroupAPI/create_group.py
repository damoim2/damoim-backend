from Repository.api.s3.s3 import AWSS3
from Repository.spi import GroupToUserRepository
from Repository.spi import GroupRepository
from damoim_service.command.GroupAPI import CreateGroup
from damoim_service.deserializer.GroupAPI.create_group_deserializer import (
    CreateGroupDeserializer,
)
from dataclasses import asdict
from damoim_service.deserializer.GroupAPI.create_group_to_user_deserializer import (
    CreateGroupToUserDeserializer,
)
from django.utils import timezone


def create_group(command: CreateGroup):
    today = timezone.now()
    s3_repo = AWSS3()
    url = None
    if command.files is not None:
        url = s3_repo.upload_file_s3(command.files)

    # group create

    group_deserializer = CreateGroupDeserializer(data=asdict(command))
    group_command = group_deserializer.create(thumbnail=url)
    group_instance = GroupRepository.create(command=group_command)

    # group_to_user_create
    group_to_user_deserializer = CreateGroupToUserDeserializer(
        data={"user_id": command.user_id}
    )
    group_to_user_command = group_to_user_deserializer.create(
        group_id=group_instance.index, today=today
    )
    GroupToUserRepository.create(group_to_user_command)
