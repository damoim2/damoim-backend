from damoim_service.command.Comment import CreateCommentCommand
from Repository.spi.Comment import create_comment
from Repository.spi.CommentToPost import create_comment_to_post
from dataclasses import asdict


def post_comment_to_post(command: CreateCommentCommand, post_id: int, user_id: int):
    comment_form = asdict(command)
    comment_instace = create_comment(form=comment_form)
    create_comment_to_post(
        comment_instace=comment_instace, post_id=post_id, user_id=user_id
    )
    return
