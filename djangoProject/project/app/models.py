from django.db import models
from django.core.validators import FileExtensionValidator

class WriteSomething(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=64, default='')
    password = models.CharField(max_length=64, default='')
    name = models.CharField(max_length=64, default='')
    github_id = models.CharField(max_length=32, default='')


class Blog(models.Model):
    blog_id = models.CharField(max_length=32)
    blog_person_id = models.IntegerField()
    blog_title = models.CharField(max_length=256)
    blog_content = models.CharField(max_length=1024)
