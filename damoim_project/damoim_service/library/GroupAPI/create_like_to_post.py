from Repository.spi import LikeToPost
from damoim_service.command.GroupAPI import PostLikeCommand


def create_like_to_post(command: PostLikeCommand):
    # return에 좋아요 갯수를 리턴해주는게 best
    if LikeToPost.has_instance_by_post_id_user_id(command=command):
        LikeToPost.delete_by_post_id_user_id(command=command)
    else:
        LikeToPost.create(command=command)
    return LikeToPost.get_count_by_post_id(post_id=command.post_id)
