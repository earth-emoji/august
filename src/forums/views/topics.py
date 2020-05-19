from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.decorators import professional_required
from forums.models import Discussion, Topic
from forums.forms import TopicForm

@login_required
@professional_required
def topic_create(request, slug):
    template_name = 'topics/form.html'
    context = {}

    if slug is None or slug == '':
        return redirect('not-found')

    discussion = Discussion.objects.get(slug=slug)

    if discussion is None:
        return redirect('not-found')

    if request.method == "POST":
        form = TopicForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.discussion = discussion
            c.moderator = request.user.professional
            c.save()
            return redirect(c.get_absolute_url())
    form = TopicForm()

    context['discussion'] = discussion
    context['form'] = form

    return render(request, template_name, context)

@login_required
@professional_required
def topic_thread(request, slug):
    template_name = 'topics/thread.html'
    context = {}

    if slug is None or slug == '':
        return redirect('not-found')

    topic = Topic.objects.get(slug=slug)

    if topic is None:
        return redirect('not-found')

    context['topic'] = topic

    return render(request, template_name, context)
