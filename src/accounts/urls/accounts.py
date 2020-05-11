from django.urls import include, path

from accounts.views import professionals, accounts

urlpatterns = [
    path('logout/', accounts.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', professionals.ProfessionalSignUpView.as_view(), name='user_signup'),
]