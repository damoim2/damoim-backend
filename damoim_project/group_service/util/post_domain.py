from group_service.models import Post
from user.models import User


def make_post_data_form(user_data: User) -> dict:
    data = Post.objects.all().order_by("created_at")
    user_datas = {
        "name": user_data.name,
        "user_id": user_data.socialtouser_set.name,
        "user_thumbnail": user_data.user_thumbnail,
    }
