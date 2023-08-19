from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("Blogs/", views.BlogHome, name="Blog"),
    path("Blogs/Recent...../", views.blogFliter1, name="BlogFil1"),
    path("Blogs/previous..../", views.blogFliter2, name="BlogFil2"),
    path("Blogs/view/", views.viewadmin, name="blogview"),
    path("<int:pk>/Blog-details/", views.DetailBlog, name="Details-Blogs"),
    path("Blogs/New-Blog/", views.BlgNewAdd, name="Blogs-Add"),
    path("Blog/<int:pk>/Edit/", views.BlgEdit, name="Blogs-Edit"),
    path("Blog/<int:pk>/deleted/", views.delete, name="Blogs-delete"),
]
