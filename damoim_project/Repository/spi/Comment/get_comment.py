from damoim_service.models import Comment


def get_comment(post_id):
    try:
        return Comment.objects.get(index=post_id)
    except Comment.DoesNotExist as e:
        return None
