from django.urls import path
from .views import CommentAPI

urlpatterns = [path("<int:post_id>", CommentAPI.as_view({"post": "create_comment"}))]
