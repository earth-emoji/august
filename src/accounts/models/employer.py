import uuid
from django.conf import settings
from django.db import models


class Employer(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="employer", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    enabled = models.BooleanField(default=False)

    @property
    def dash_url(self):
        return "/dashboard/%s/" % (self.slug)

    def __str__(self):
        return self.company_name