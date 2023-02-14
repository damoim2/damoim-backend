from django.urls import include, path
from .views import LogoutView, Login, Register, RefreshAPI

urlpatterns = [
    path('login', Login.as_view),
    path('logout', LogoutView.as_view),
    path('registration', Register.as_view),
    path('refresh', RefreshAPI.as_view),
]