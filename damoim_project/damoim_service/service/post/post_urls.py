from django.urls import path
from .views import PostAPI

urlpatterns = [
    path("", PostAPI.as_view({"post": "post_post"})),
    path("list/", PostAPI.as_view({"get": "get_list"})),
    path("like/<int:post_id>", PostAPI.as_view({"post": "post_like"})),
]
