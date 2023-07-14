from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('SkillsCategory', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    time = models.ForeignKey('SkillsTime', on_delete=models.CASCADE)
    rate = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True, null=True)

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