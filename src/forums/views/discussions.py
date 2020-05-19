from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.decorators import professional_required
from forums.models import Discussion

@login_required
@professional_required
def discussion_list(request):
    template_name = 'discussions/list.html'
    context = {}
    discussions = Discussion.objects.all()
    context["discussions"] = discussions
    return render(request, template_name, context)

@login_required
@professional_required
def discussion_details(request, slug):
    template_name = 'discussions/details.html'
    context = {}

    if slug is None or slug == '':
        return redirect('not-found')

    discussion = Discussion.objects.get(slug=slug)

    if discussion is None:
        return redirect('not-found')

    context['discussion'] = discussion

    return render(request, template_name, context)
