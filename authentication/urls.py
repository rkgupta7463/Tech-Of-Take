from django.urls import path, include
from .views import *

urlpatterns = [
    path("signin/", loginUser, name="signin"),
    path("signup/", signinUser, name="signup"),
    path("signout/", logOutUser, name="signout"),
]
