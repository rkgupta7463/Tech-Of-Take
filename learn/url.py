from django.contrib import admin
from django.urls import path
from learn.views import *

urlpatterns = [
    path("learning/",learning, name="Learn_platfrom"),
    path("New/Course-Add/",AddLearning, name="addlearn"),
    path("course/view/",viewadmin, name="view"),
    path("course/<int:pk>/update/",updatecourse, name="update"),
    path("course/<int:pk>/delete/",deletecourse, name="delete"),
    path("trending/",trending, name="trending_IT"),
]