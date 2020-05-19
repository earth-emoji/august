from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import Professional
from jobs.forms import ReferenceForm
from jobs.models import Reference
from users.decorators import professional_required

@login_required
@professional_required
def reference_list(request):
    template_name = 'references/list.html'
    context = {}
    references = Reference.objects.filter(professional=request.user.professional)
    context["references"] = references
    return render(request, template_name, context)

@login_required
@professional_required
def reference_create(request):
    template_name = 'references/form.html'
    context = {}
    if request.method == 'POST':
        form = ReferenceForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.professional = request.user.professional
            c.save()
            return redirect('references:list')
    else:
        form = ReferenceForm()
    context['form'] = form
    return render(request, template_name, context)
