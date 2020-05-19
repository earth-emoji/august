from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework import status

from accounts.models import Professional
from jobs.forms import EducationHistoryForm
from jobs.models import EducationHistory
from jobs.serializers import EducationHistorySerializer
from users.decorators import professional_required

@login_required
@professional_required
def edu_histories(request):
    template_name = 'education_history/list.html'
    context = {}

    education_history = EducationHistory.objects.filter(professional=request.user.professional)

    context["education_history"] = education_history
    return render(request, template_name, context)

@login_required
@professional_required
def edu_create(request):
    template_name = 'education_history/form.html'
    context = {}
    if request.method == 'POST':
        form = EducationHistoryForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.professional = request.user.professional
            c.save()
            return redirect('education-history:list')
    else:
        form = EducationHistoryForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
@professional_required
@api_view(['GET', 'POST'])
def edu_collection(request):

    if request.method == 'GET':
        education_history = EducationHistory.objects.filter(professional=request.user.professional)
        serializer = EducationHistorySerializer(education_history, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = {
            'school_name': request.data.get('school_name'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'did_complete': request.data.get('did_complete'),
            'certificate': request.data.get('certificate'),
            'professional': request.user.professional.pk
        }
        serializer = EducationHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
