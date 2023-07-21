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

####


class Comment(models.Model):
    post = models.ForeignKey(Blog,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)