from django.contrib import admin

from jobs.models import Job, WorkHistory, EducationHistory, Reference

admin.site.register(Job)
admin.site.register(WorkHistory)
admin.site.register(EducationHistory)
admin.site.register(Reference)
