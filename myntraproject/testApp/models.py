from django.db import models

# Create your models here.
class buyer(models.Model):
    name=models.CharField(max_length=128)
    gender=models.CharField(max_length=128)
    location=models.CharField(max_length=1000)
