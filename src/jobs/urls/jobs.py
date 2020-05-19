from django.urls import include, path

from jobs import views

urlpatterns = [
    path('jobs/', include(([
        path('', views.public_jobs, name='list'),
        path('create/', views.create_job, name='create'),
        path('<slug:slug>/apply/', views.apply, name="apply"),
        path('<slug:slug>/details/', views.job_details, name="details"),
        path('<slug:slug>/view/', views.employer_job_view, name="employer-view"),
    ], 'jobs'))),
]
