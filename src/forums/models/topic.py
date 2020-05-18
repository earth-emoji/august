import uuid
from django.db import models

from accounts.models import Professional
from classifications.models import Tag

class Topic(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='topics', blank=True)
    moderator = models.ForeignKey(Professional, on_delete=models.ForeignKey, related_name='topics', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'