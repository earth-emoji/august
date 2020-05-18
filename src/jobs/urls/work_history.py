from django.urls import include, path

from jobs import views

urlpatterns = [
    path('work-history/', include(([
        path('<uuid:slug>/', views.work_histories, name='list'),
    ], 'work-history'))),
    path('api/work-history/', include(([
        path('', views.work_collection, name='collection'),
    ], 'api-work-history'))),
]
