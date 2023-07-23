from damoim_service.models import Comment


def delete_comment(post_id):
    try:
        instance = Comment.objects.get(index=post_id)
        instance.delete()
        return True
    except Comment.DoesNotExist as e:
        return False
