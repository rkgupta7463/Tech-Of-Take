from django.contrib import admin
from django.urls import path, include
from blog.url import *
# from home.views  import  *
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView
from .views import *

urlpatterns = [
    path("",Home, name="Home"),
    path("cruddata/1/crudapplication/",cruddata, name="crud"),
    path("blogging/2/blogging/",blogging, name="blogsapp"),
    path("weather/3/weather/",weather, name="weatherapp"),
    path("image-uploader/4/weather/",imageup, name="imageUp"),
    path("cars/5/car-price-predictor/",car_price_pred, name="car_pred"),
    path("password-reset/", PasswordResetView.as_view(template_name="auth/forgetpass.html"), name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name="auth/pass_reset_sent.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name="auth/pass_reset_confirm.html"),name="password_reset_confirm"),
    path("password-reset-complete/",PasswordResetCompleteView.as_view(template_name="auth/pass_reset_done.html"),name="password_reset_complete"),
    path("<int:pk>/show-more/",showmore, name="show-more"),
    path("<int:pk>/Project-view-more/",showproject, name="Proj_View"),
    path("<int:pk>/feature-view-more/",include("blog.url")),
]