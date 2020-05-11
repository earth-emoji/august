from django.urls import include, path

from accounts.views import professionals

urlpatterns = [
    path('', include(([
        path('professionals/<uuid:slug>/', professionals.professional_profile, name='profile'),
    ], 'professionals')))
]
