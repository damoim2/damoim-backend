from damoim_service.command.GroupToUser import CreateGroupToUserCommand
from damoim_service.models import GroupToUser


def create(command: CreateGroupToUserCommand):
    return GroupToUser.objects.create(
        user_id_id=command.user_id, group_id_id=command.group_id
    )
