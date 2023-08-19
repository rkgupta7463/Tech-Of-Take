from django.db import models
from django.contrib.auth.models import User

class ProfileUserImg(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_images')
    file = models.ImageField(upload_to='profile_images/', blank=True)
