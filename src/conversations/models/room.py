from datetime import datetime
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from classifications.models import Category, Tag
from conversations.choices import VISIBILITY_CHOICES

class Room(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rooms", blank=True)
    name = models.CharField(max_length=60, unique=True, blank=True)
    details = models.TextField(default='', blank=True)
    access = models.CharField(max_length=9, choices=VISIBILITY_CHOICES, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="room_memberships", blank=True)
    black_list = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="rooms_forbidden", blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="rooms", null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="rooms", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        today = datetime.today()
        title_slugified = slugify(self.name)
        self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)