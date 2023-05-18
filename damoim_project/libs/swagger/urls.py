from django.urls import path, include
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from auth.urls import urlpatterns as auth_urls
from damoim_service.urls import urlpatterns as service_urls

swagger_auth_urls = [
    path("auth/", include(auth_urls)),
]
swagger_service_urls = [
    path("api/", include(service_urls)),
]
swagger_auth_urls = SpectacularJSONAPIView.as_view(patterns=swagger_auth_urls)
swagger_service_urls = SpectacularJSONAPIView.as_view(patterns=swagger_service_urls)
json_urls = [
    path("auth/", swagger_auth_urls, name="auth"),
    path("api/", swagger_service_urls, name="service"),
]
swagger_view_urls = [
    path(
        "auth/",
        SpectacularSwaggerView.as_view(url_name="auth"),
        name="swagger-ui",
    ),
    path(
        "api/",
        SpectacularSwaggerView.as_view(url_name="service"),
        name="swagger-ui",
    ),
]
redoc_urls = [
    path(
        "auth/",
        SpectacularRedocView.as_view(url_name="auth"),
        name="auth-redoc",
    ),
    path(
        "api/",
        SpectacularRedocView.as_view(url_name="service"),
        name="auth-redoc",
    ),
]

urlpatterns = [
    path("docs/json", include(json_urls)),
    path("docs/", include(swagger_view_urls)),
    path("redoc/", include(redoc_urls)),
]
