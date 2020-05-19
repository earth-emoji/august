from django.urls import include, path

from jobs import views

urlpatterns = [
    path('work-history/', include(([
        path('', views.work_histories, name='list'),
        path('create/', views.work_create, name='create'),
    ], 'work-history'))),
    path('api/work-history/', include(([
        path('', views.work_collection, name='collection'),
    ], 'api-work-history'))),
]
