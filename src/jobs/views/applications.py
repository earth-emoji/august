from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from jobs.models import Job, Application
from accounts.models import Employer, Professional
from users.decorators import employer_required, professional_required


@login_required
@professional_required
def apply(request, slug):

    if slug is None:
        return Http404

    job = Job.objects.get(slug=slug)

    if job is None:
        return Http404

    if request.method == 'POST':
        interest = request.POST['interest']
        qualifications = request.POST.getlist('qualifications')
        Application.objects.create(
            job=job, applicant=request.user.professional, status="Pending", interest=interest, qualifications=qualifications)
        data = {'success' : True, 'message': 'Your application has been submitted!'}
        return JsonResponse(data)

    return HttpResponse('')
