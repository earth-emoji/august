from django.urls import include, path

from jobs import views

urlpatterns = [
    path('education-history/', include(([
        path('', views.edu_histories, name='list'),
        path('create/', views.edu_create, name='create'),
    ], 'education-history'))),
    path('api/education-history/', include(([
        path('', views.edu_collection, name='collection'),
    ], 'api-education-history'))),
]
