from django.urls import include, path

from . import views

urlpatterns = [
    path('documents/', include(([
        path('', views.DocumentUploadView.as_view(), name='list'),
    ], 'documents')))
]
