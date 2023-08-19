from django.db import models

# Create your models here.
class Resume(models.Model):
    resumes=models.FileField(upload_to="image/pdf")