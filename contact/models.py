from django.db import models

# Create your models here.
class ContactModel(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.EmailField(max_length=30)
    umessage=models.TextField()

    def __str__(self):
        return self.uname