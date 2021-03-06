from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from users.decorators import professional_required
from forums.models import Post, Comment
from forums.serializers import CommentSerializer, ReplySerializer

@login_required
@professional_required
@api_view(['GET', 'POST'])
def comment_collection(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'Record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = {
            'content': request.data.get('c-content'),
            'post_pk': post.pk,
            'author_pk': request.user.professional.pk
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@professional_required
@api_view(['GET', 'POST'])
def reply_collection(request, slug):
    try:
        comment = Comment.objects.get(slug=slug)
    except Comment.DoesNotExist:
        return JsonResponse({'message': 'Record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        replies = Comment.objects.filter(parent=comment).order_by('-created_at')
        serializer = ReplySerializer(replies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = {
            'content': request.data.get('reply-content'),
            'post_pk': comment.post.pk,
            'author_pk': request.user.professional.pk,
            'parent_pk': comment.pk,
        }
        serializer = ReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)