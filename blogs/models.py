from django.db import models

# Create your models here.

class Blog(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    char=models.TextField()
    image=models.ImageField(upload_to='image/')


    def __str__(self):
        return self.text

    def date_time(self):
        return  self.date.strftime('%m %d %Y')

    def summary(self):
        return self.char[:50]