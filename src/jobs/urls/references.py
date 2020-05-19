from django.urls import include, path

from jobs import views

urlpatterns = [
    path('references/', include(([
        path('', views.reference_list, name='list'),
        path('create/', views.reference_create, name='create'),
    ], 'references')))
]
