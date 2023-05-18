from Repository.spi import GroupToUserRepository
from damoim_service.command.GroupToUser import CreateGroupToUserCommand


def map_user_to_group(command: CreateGroupToUserCommand):
    return GroupToUserRepository.create(command)
