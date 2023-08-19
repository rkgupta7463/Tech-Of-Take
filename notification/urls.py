from django.urls import path
from .views import notify
urlpatterns = [
    path("notify/",notify, name="notifies")
]