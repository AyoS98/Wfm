from django.db import models

# Create your models here.
class Info(models.Model):
    title = models.CharField(max_length=100, null=True)
    info = models.TextField(max_length=300, null=True)
    image = models.ImageField(upload_to='media')

    
class WfmAnonContactsubmission(models.Model):
        subject = models.CharField(max_length=200, null=True)
        message = models.TextField(null=True)