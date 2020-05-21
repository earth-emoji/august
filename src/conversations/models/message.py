import uuid
from django.conf import settings
from django.db import models

from conversations.models import Room

class Message(models.Model):
    slug        = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    room        = models.ForeignKey(Room, blank=True, on_delete=models.CASCADE, related_name='messages')
    sender      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.email}"