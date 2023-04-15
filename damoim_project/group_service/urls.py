from group_service.group_view.group_post_service import PostViewSet
from django.urls import include, path

url_patterns = [
    path(
        PostViewSet.as_view(
            {"post": "create", "get": "get", "update": "update", "delete": "delete"}
        )
    )
]
