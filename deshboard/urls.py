from django.urls import path
from .views import *
urlpatterns = [
    path("dashboard/",desh, name="dashboard"),
    path("profile/<int:pk>/view/",profile_view, name="profileview"),
    path("profile/Edit/",EditProfile, name="profileEdit"),
    path("User/change-password/",UserPassChange, name="change-password"),
    path("users/list/",usersList, name="userslist"),
    path("New-users/Add/",usersAddFun, name="useradd"),
    path("user/<int:pk>/deleted/",userdelete, name="userdel"),
    path("users/<int:pk>/profile/Edit/",usersproEdit, name="usersproEdit"),
]