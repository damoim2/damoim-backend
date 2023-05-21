from damoim_service.command.Post import CreatePostCommand


def create_post(command: CreatePostCommand):
    from damoim_service.models import Post

    return Post.objects.create(
        user_id=command.user_id,
        group_id_id=command.group_id_id,
        title=command.title,
        contents=command.contents,
    )
