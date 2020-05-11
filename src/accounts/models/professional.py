import uuid
from django.conf import settings
from django.db import models


class Professional(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="professional", on_delete=models.CASCADE)

    @property
    def dash_url(self):
        return "/dashboard/%s/" % (self.slug)

    def __str__(self):
        return self.user.email