from django.db import models
from skills.models import Skills
from django.contrib.auth.models import User


class Request(models.Model):
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='request_skill')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_user')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_receiver')
    REQUEST_CHOICES = (
        ('accepted', 'accepted'),
        ('pending', 'pending'),
    )
    status = models.CharField(choices=REQUEST_CHOICES, max_length=100)
    date = models.DateField()
    time = models.TimeField()
    create = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.skill.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"