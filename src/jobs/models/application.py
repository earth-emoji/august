import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models

from accounts.models import Employer, Professional
from jobs.choices import APPLICATION_STATUS_CHOICES

from .job import Job

class Application(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants", blank=True)
    applicant = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="applications", blank=True)
    interest = models.TextField(blank=True)
    qualifications = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    @property
    def match(self):
        return len(set(self.job.skills) & set(self.qualifications)) / float(len(set(self.job.skills) | set(self.qualifications))) * 100

    @property
    def public_url(self):
        return "/applications/view/%s/" % (self.slug)

    @property
    def edit_url(self):
        return "/applications/edit/%s/" % (self.slug)

    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'

    def __str__(self):
        return f"{self.job.name}: {self.applicant.user.name}"
