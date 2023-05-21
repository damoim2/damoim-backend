from damoim_service.command.GroupAPI import PostLikeCommand
from damoim_service.models import LikeToPost


def delete_by_post_id_user_id(command: PostLikeCommand):
    instance = LikeToPost.objects.get(
        post_id_id=command.post_id, user_id_id=command.user_id
    )
    instance.delete()
    return
