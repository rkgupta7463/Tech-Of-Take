from django.db import models

# Create your models here.
class TestiminalModel(models.Model):
    cname=models.CharField(max_length=50)
    ctitle=models.CharField(max_length=75)
    cemail=models.CharField(max_length=30)
    cphone=models.CharField(max_length=10)
    cfeedback=models.TextField()
    cfdate=models.DateTimeField(auto_now=True)
    cfdatemodification=models.DateTimeField(auto_now_add=True)    

    # def __init__(self):
    #     print(self.ctitle)
    #     return self.ctitle