from damoim_service.command.Comment import CreateCommentCommand


def create_comment(command: CreateCommentCommand):
    from damoim_service.models import Comment

    return Comment.objects.create(
        user_id_id=command.user_id,
        comment=command.comment,
    )
