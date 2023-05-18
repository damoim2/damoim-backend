from django.urls import path
from .views import CommentAPI

urlpatterns = [path("", CommentAPI.as_view({"post": "create_comment"}))]
