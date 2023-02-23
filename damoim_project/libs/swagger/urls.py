from django.conf.urls import include
from django.urls import path
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularRedocView,
    SpectacularJSONAPIView,
)
from damoim_project.user import urls as user_urls

swagger_user_urls = [path("auth/",include(user_urls))]

swagger_user_urls = SpectacularJSONAPIView.as_view(patterns=swagger_user_urls)

json_urls = [
    path("auth", swagger_user_urls, name="auth"),
]

swagger_view_urls = [
    path(
        "auth",
        SpectacularSwaggerView.as_view(url_name="auth"),
        name="swagger-ui",
    )
]

redoc_urls = [
    path(
        "auth",
        SpectacularRedocView.as_view(url_name="auth"),
        name="auth-redoc",
    ),
]

urlpatterns = [
    path("docs/json", include(json_urls)),
    path("docs/", include(swagger_view_urls)),
    path("redoc/", include(redoc_urls)),
]