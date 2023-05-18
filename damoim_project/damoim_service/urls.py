from django.urls import path, include
from .service import post_url, group_url, comment_url

urlpatterns = [
    path("post/", include(post_url)),
    path("group/", include(group_url)),
    path("comment/", include(comment_url)),
]
