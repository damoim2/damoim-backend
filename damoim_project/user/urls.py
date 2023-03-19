from django.urls import include, path
from user.views import SignIn, SignUp, SignOut, Refresh

urlpatterns = [
    path("login", SignIn.as_view({"post": "post"})),
    path("logout", SignOut.as_view({"post": "post"})),
    path("registration", SignUp.as_view({"post": "post"})),
    path("refresh", Refresh.as_view({"post": "post"})),
]
