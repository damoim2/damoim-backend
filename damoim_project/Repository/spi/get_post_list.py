from Repository import PostToImage, Post
from Repository.LikeToPost import LikeToPost
from django.db.models import F, Count


def get_post_list_combo(page: int, uuid):
    start = 10 * (page - 1)
    end = 10 * page
    post = Post.objects.all()[start:end]
    formal_data = post.annotate(
        like_count=Count(F("liketopost__index")),
        comment_count=Count(F("commenttopost__index")),
        is_like=False,
        is_editable=True if F("user_id_id") == uuid else False,
    ).values(
        "index",
        "user_id__name",
        "user_id_id",
        "user_id__thumbnail",
        "contents",
        "created_at",
        "like_count",
        "comment_count",
        "is_editable",
        "is_like",
    )
    data_form = []
    for i in post:
        if LikeToPost.objects.filter(post_id_id=i["index"], user_id_id=uuid).exists():
            i["is_like"] = True
        list = PostToImage.objects.filter(post_id_id=i["index"]).values("image_url")
        image = []
        for j in list:
            image.append(j["image_url"])
        data_form.append(
            {
                "user": {
                    "name": i["user_id__name"],
                    "user_id": i["user_id_id"],
                    "user_thumbnail": i["user_id__thumbnail"],
                },
                "post": {
                    "contents": i["contents"],
                    "date": i["created_at"],
                    "like_count": i["like_count"],
                    "comment_count": i["comment_count"],
                    "thumbnail": image,
                },
                "is_like": i["is_liked"],
                "is_editable": i["is_editable"],
            }
        )
