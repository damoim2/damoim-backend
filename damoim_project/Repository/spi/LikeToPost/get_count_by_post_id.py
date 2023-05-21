from damoim_service.models import LikeToPost


def get_count_by_post_id(post_id: int) -> int:
    return LikeToPost.objects.filter(post_id_id=post_id).count()
