from damoim_service.models import Comment, CommentToPost


def create_comment_to_post(comment_instace: Comment, post_id: int, user_id: int):
    return CommentToPost.objects.create(
        comment_id=comment_instace, post_id_id=post_id, user_id_id=user_id
    )
