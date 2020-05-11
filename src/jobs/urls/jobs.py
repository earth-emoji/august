from django.urls import include, path

from jobs import views

urlpatterns = [
    path('jobs/', include(([
        path('', views.public_jobs, name='list'),
        path('create/', views.create_job, name='create'),
        path('<uuid:slug>/apply/', views.apply, name="apply"),
        path('<uuid:slug>/details/', views.job_details, name="details"),
        path('<uuid:slug>/view/', views.employer_job_view, name="employer-view"),
        # path('<uuid:slug>/update/', views.employer_job_update, name="employer-job-update")
    ], 'jobs'))),
]
