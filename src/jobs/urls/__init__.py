from django.urls import path, include

urlpatterns = [
    path('', include('jobs.urls.jobs')),
    path('', include('jobs.urls.work_history')),
    path('', include('jobs.urls.education_history')),
    path('', include('jobs.urls.references')),
]