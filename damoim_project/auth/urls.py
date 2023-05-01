from django.urls import path
from .views import RefreshView, LoginView, LogoutView, RegistrationView

urlpatterns = [
    path("auth/register/", RegistrationView.as_view()),
    path("auth/login/", LoginView.as_view()),
    path("auth/refresh/", RefreshView.as_view()),
    path("auth/logout/", LogoutView.as_view()),
]
