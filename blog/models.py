from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100, default="Admin")

    def __str__(self):
        return self.title

