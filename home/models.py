from django.db import models

# Create your models here.
class InterestArea(models.Model):
    image = models.ImageField(upload_to='media/')
    title=models.CharField(max_length=150)
    descrp=models.TextField()

    def __str__(self):
        return self.title


class ProjectModel(models.Model):
    proj_image = models.ImageField(upload_to='media/')
    proj_title=models.CharField(max_length=100)
    proj_descript=models.TextField()
    proj_link=models.URLField()
    def __str__(self):
        return self.proj_title

class FeartureSection(models.Model):
    FeaImage=models.ImageField(upload_to="media/")
    FeaTitle=models.CharField(max_length=100)
    FeaDescript=models.TextField()
    FeaWebLink=models.CharField(max_length=50,default=None, null=True , blank=True)

    def __str__(self):
        return self.FeaTitle