from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse

from jobs.forms import JobForm
from jobs.models import Job, Application
from accounts.models import Employer
from users.decorators import employer_required, professional_required

@login_required
@employer_required
def employer_jobs(request, slug):
    template_name = 'jobs/elist.html'
    context = {}

    if slug is None:
        return redirect('not-found')

    creator = Employer.objects.get(slug=slug)

    if creator is None:
        return redirect('not-found')

    if not (creator == request.user.employer):
        return redirect('forbidden')

    jobs = Job.objects.filter(creator=creator)
    context["jobs"] = jobs

    return render(request, template_name, context)


@login_required
@employer_required
def employer_job_view(request, slug):
    template_name = 'jobs/edetails.html'
    context = {}

    if slug is None:
        return redirect('not-found')

    job = Job.objects.get(slug=slug)

    if job is None:
        return redirect('not-found')

    if not (job.creator == request.user.employer):
        return redirect('forbidden')

    applicants = sorted(Application.objects.filter(job=job), reverse=True, key=lambda t: t.match)

    context["job"] = job
    context["applicants"] = applicants

    return render(request, template_name, context)

@login_required
@employer_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            c = form.save(commit=False)
            c.creator = request.user.employer
            c.save()
            return redirect('employers:employer-jobs', request.user.employer.slug)
    else:
        form = JobForm()
    return render(request, 'jobs/form.html', {'form': form})

@login_required
@professional_required
def public_jobs(request):
    template_name = 'jobs/list.html'
    context = {}
    jobs = Job.objects.all()
    context["jobs"] = jobs
    return render(request, template_name, context)

@login_required
@professional_required
def job_details(request, slug):
    template_name = 'jobs/details.html'
    context = {}

    if slug is None:
        return redirect('not-found')

    job = Job.objects.get(slug=slug)

    if job is None:
        return redirect('not-found')

    context["job"] = job
    return render(request, template_name, context)
