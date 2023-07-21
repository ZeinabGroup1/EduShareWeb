from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    phone = models.IntegerField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='media/owner_profile/', default='media/default_images/avatar.png')

    def __str__(self):
        return self.user.username

    @property
    def complete(self):
        if self.phone is not None and self.first_name is not None and self.last_name is not None and self.country and self.city is not None and self.address is not None:
            return True
        else:
            return False


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=User)


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.user.username
