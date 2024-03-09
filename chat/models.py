from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Message(models.Model):
    room_name = models.CharField(max_length=255)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)