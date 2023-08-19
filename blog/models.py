from distutils.command.upload import upload
from turtle import title
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class BlogPost(models.Model):
    image=models.ImageField(upload_to="media/", max_length=250, null=True, default=None, blank=True)
    title=models.CharField(max_length=150)
    discription=models.TextField()
    web_link=models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete= models.CASCADE,related_name='BlogPost')
    date_time=models.DateTimeField(auto_now=True)
    modification=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    Umessage=models.TextField()
    uname=models.CharField(max_length=50)
    uemail=models.EmailField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
# Create your models here.
