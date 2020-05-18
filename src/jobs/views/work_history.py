from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import Professional
from jobs.models import WorkHistory
from jobs.serializers import WorkHistorySerializer
from users.decorators import professional_required

@login_required
@professional_required
def work_histories(request, slug):
    template_name = 'work_history/list.html'
    context = {}

    if slug is None or slug == "":
        return redirect('not-found')

    professional = Professional.objects.get(slug=slug)

    if professional is None:
        return redirect('not-found')

    context["professional"] = professional
    return render(request, template_name, context)

@login_required
@professional_required
@api_view(['GET', 'POST'])
def work_collection(request):

    if request.method == 'GET':
        work_history = WorkHistory.objects.filter(professional=request.user.professional)
        serializer = WorkHistorySerializer(work_history, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'employer_name': request.data.get('employer_name'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'job_title': request.data.get('job_title'),
            'duties': request.data.get('duties'),
            'professional': request.user.professional.pk
        }
        serializer = WorkHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
