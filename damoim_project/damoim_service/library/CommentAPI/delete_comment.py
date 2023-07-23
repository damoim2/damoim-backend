from Repository.spi.Comment import delete_comment, get_comment
from libs.Exception import NoAuthority, DamoimServerExceptionError


def delete(post_id, user_id):
    comment_instance = get_comment(post_id=post_id)
    if comment_instance.user_id_id == user_id:
        result = delete_comment(post_id=post_id)
        if result is None:
            raise DamoimServerExceptionError()
        return True
    else:
        # 권한이 없음 자신의 글이 아님
        raise NoAuthority()
