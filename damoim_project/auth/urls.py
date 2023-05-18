from django.urls import path
from .views import RefreshView, LoginView, LogoutView, RegistrationView

urlpatterns = [
    path("register/", RegistrationView.as_view({"post": "create"})),
    path("login/", LoginView.as_view()),
    path("refresh/", RefreshView.as_view()),
    path("logout/", LogoutView.as_view()),
]
