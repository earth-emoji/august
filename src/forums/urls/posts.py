from django.urls import include, path

from forums import views

urlpatterns = [
    path('api/posts/', include(([
        path('<uuid:slug>/comment/', views.comment_collection, name='comment'),
    ], 'posts-api'))),
]