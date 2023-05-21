from damoim_service.models import Comment, CommentToPost


def create_comment_to_post(comment_instace: Comment, post_id: int):
    # 해당 테이블에 user_id가 들어가는건 불필요 요소인것 같은데 생각해보기
    return CommentToPost.objects.create(
        comment_id=comment_instace, post_id_id=post_id, user_id=comment_instace.user_id
    )
