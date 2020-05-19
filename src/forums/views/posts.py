from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.decorators import professional_required
from forums.models import Topic, Post
from forums.serializers import PostSerializer

@login_required
@professional_required
@api_view(['GET', 'POST'])
def post_collection(request, slug):
    try:
        topic = Topic.objects.get(slug=slug)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = Post.objects.filter(topic=topic).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'content': request.data.get('content'),
            'topic_pk': topic.pk,
            'author_pk': request.user.professional.pk
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


