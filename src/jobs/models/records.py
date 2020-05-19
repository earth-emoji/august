from django.db import models

from accounts.models import Professional
from jobs.choices import KNOWN_MEASURE_CHOICES, REFERENCE_TYPE_CHOICES

class WorkHistory(models.Model):
    employer_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    duties = models.TextField(blank=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='work_history', blank=True)

    def __str__(self):
        return f"{self.professional.user.name} at {self.employer_name}"

    class Meta:
        verbose_name = 'work history'
        verbose_name_plural = 'work histories'

class EducationHistory(models.Model):
    school_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    did_complete = models.BooleanField(blank=True)
    certificate = models.CharField(max_length=100, blank=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='education_history', blank=True)

    def __str__(self):
        return f"{self.professional.user.name} at {self.school_name}"

    class Meta:
        verbose_name = 'education history'
        verbose_name_plural = 'education histories'

class Reference(models.Model):
    name = models.CharField(max_length=100, blank=True)
    known_span = models.PositiveIntegerField(blank=True)
    known_measure = models.CharField(max_length=15, choices=KNOWN_MEASURE_CHOICES, blank=True)
    contact_info = models.CharField(max_length=60, blank=True)
    reference_type = models.CharField(max_length=15, choices=REFERENCE_TYPE_CHOICES, blank=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='references', blank=True)
    
    def __str__(self):
        return f"{self.professional.user.name} ref {self.name}"

    class Meta:
        verbose_name = 'reference'
        verbose_name_plural = 'references'
