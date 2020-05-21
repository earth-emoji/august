import uuid
from django.conf import settings
from django.db import models

from conversations.models import Room
from conversations.choices import REQUEST_TYPE_CHOICES

class RoomRequest(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    # user requesting
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='requests_sent', on_delete=models.CASCADE)
    
    # user requested
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='requests_received' , on_delete=models.CASCADE)

    room = models.ForeignKey(Room, related_name='requests', on_delete=models.CASCADE)
    
    # status
    status = models.BooleanField(default=False)

    type = models.CharField(max_length=9, choices=REQUEST_TYPE_CHOICES, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)