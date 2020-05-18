import uuid
from django.db import models

from accounts.models import Professional

class Post(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Professional, on_delete=models.ForeignKey, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.email

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'