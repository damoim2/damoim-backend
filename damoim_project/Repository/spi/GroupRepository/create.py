from damoim_service.command.Group import CreateGroupCommand


def create(command: CreateGroupCommand):
    from damoim_service.models import Group

    return Group.objects.create(
        name=command.name,
        owner_id=command.owner,
        thumbnail=command.thumbnail,
    )
