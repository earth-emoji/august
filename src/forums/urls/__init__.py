from django.urls import path, include

urlpatterns = [
    path('', include('forums.urls.discussions')),
]