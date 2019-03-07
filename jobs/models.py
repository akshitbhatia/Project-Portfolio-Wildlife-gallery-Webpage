from django.db import models

# Create your models here.

class Job(models.Model):
    image=models.ImageField(upload_to='image/')
    char=models.CharField(max_length=250)

