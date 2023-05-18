def create_comment(form: dict):
    from damoim_service.models import Comment

    return Comment.objects.create(
        user_id=form["user_id"],
        comment=form["comment"],
    )
