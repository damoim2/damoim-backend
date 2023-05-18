from django.urls import path
from .views import GroupAPI

urlpatterns = [
    path("", GroupAPI.as_view({"post": "create"})),
    path("list/", GroupAPI.as_view({"get": "get_group_list"})),
    path("member", GroupAPI.as_view({"post": "map_user_group"})),
    path(
        "member/list/<int:group_id>", GroupAPI.as_view({"get": "get_group_member_list"})
    ),
]
