from django.urls import include, path

from forums import views

urlpatterns = [
    path('topics/', include(([
        path('<slug:slug>/', views.topic_thread, name='thread'),
    ], 'topics'))),
    path('api/topics/', include(([
        path('<slug:slug>/posts', views.post_collection, name='posts'),
    ], 'topics-api'))),
]
