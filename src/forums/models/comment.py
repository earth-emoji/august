import uuid
from django.db import models
from django.shortcuts import reverse
from accounts.models import Professional
from forums.models import Post

class Comment(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='comments', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
