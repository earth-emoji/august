import uuid
from django.db import models

class Forum(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=60, unique=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'forum'
        verbose_name_plural = 'forums'

