from django.db import models
from django.core.validators import FileExtensionValidator

class WriteSomething(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.title
