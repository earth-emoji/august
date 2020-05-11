import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models

from accounts.models import Employer

class Job(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    external_url = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.CharField(max_length=255, null=True, blank=True)
    employment_type = models.CharField(max_length=255, null=True, blank=True)
    pay_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    published = models.BooleanField(default=False, blank=True)
    is_featured = models.BooleanField(default=False, blank=True)
    is_expired = models.BooleanField(default=False, blank=True)
    apply_here = models.BooleanField(default=False, blank=True)
    apply_instructions = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    positions_to_fill = models.PositiveIntegerField(blank=True)
    skills = ArrayField(models.CharField(max_length=3000), null=True, blank=True)
    creator = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs', blank=True)

    @property
    def public_url(self):
        return "/jobs/view/%s/" % (self.slug)

    @property
    def edit_url(self):
        return "/jobs/edit/%s/" % (self.slug)

    @property
    def apply_url(self):
        return "/jobs/%s/apply/" % (self.slug)

    class Meta:
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

    def __str__(self):
        return self.name