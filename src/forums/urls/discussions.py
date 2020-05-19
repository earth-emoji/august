from django.urls import include, path

from forums import views

urlpatterns = [
    path('discussions/', include(([
        path('', views.discussion_list, name='list'),
        path('<slug:slug>/', views.discussion_details, name='details')
    ], 'discussions'))),
]
