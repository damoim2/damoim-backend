from damoim_service.command.GroupAPI import PostLikeCommand
from damoim_service.models import LikeToPost


def create(command: PostLikeCommand):
    return LikeToPost.objects.create(
        user_id_id=command.user_id,
        post_id_id=command.post_id,
    )
