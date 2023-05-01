from django.urls import path
from .mock_views import MockMyProfileView, MockHomeView, MockPostView

urlpatterns = [
    path("home/group/", MockHomeView.as_view({"get": "test_get_group_list"})),
    path("home/schedule/", MockHomeView.as_view({"get": "test_get_schedule"})),
    path("profile/", MockMyProfileView.as_view({"get": "test_get_my_info"})),
    path("post/list/", MockPostView.as_view({"get": "test_get_list"})),
    path("post/", MockPostView.as_view({"get": "test_get_detail"})),
]
