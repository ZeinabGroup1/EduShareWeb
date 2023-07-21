from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('SkillsCategory', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    time = models.ForeignKey('SkillsTime', on_delete=models.CASCADE)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True, null=True)
    like = models.ManyToManyField(User, related_name='skills_like',null=True,blank=True)
    rating = models.ManyToManyField('Rate',related_name='skills_rating',null=True,blank=True)

    def __str__(self):
        return self.title


class SkillsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SkillsTime(models.Model):
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.time


class Rate(models.Model):
    rate = models.PositiveIntegerField()

    def __str__(self):
        return f'rate is {str(self.rate)}'
