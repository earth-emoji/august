from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls.accounts')),
    path('', include('accounts.urls.employers')),
    path('', include('accounts.urls.professionals')),
]