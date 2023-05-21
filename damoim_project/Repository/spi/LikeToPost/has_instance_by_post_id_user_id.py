from damoim_service.command.GroupAPI import PostLikeCommand
from damoim_service.models import LikeToPost


def has_instance_by_post_id_user_id(command: PostLikeCommand):
    return LikeToPost.objects.filter(
        user_id_id=command.user_id, post_id_id=command.post_id
    ).exists()
