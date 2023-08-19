from django.db import models
# Create your models here.

class CourseLearn(models.Model):
    title=models.CharField(max_length=100)
    CourseImage=models.ImageField(upload_to='image/courseImg')
    description=models.TextField()
    web_link_learn=models.URLField(default=None, null=True, blank=True)
    doc_link_learn=models.URLField(default=None, null=True, blank=True)
    video_learn=models.URLField(default=None, null=True , blank=True)
    scription_learn=models.URLField(default=None, null=True, blank=True)
    def __str__(self):
        return self.title


class TrendingModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="media/")
    weblink=models.URLField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title
