from collections import OrderedDict

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView

from accounts.forms.professionals import ProfessionalSignUpForm
from accounts.models import Professional
from users.decorators import professional_required
from users.models import User


class ProfessionalSignUpView(CreateView):
    model = User
    form_class = ProfessionalSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Candidate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('professionals:profile', user.slug)

@login_required
@professional_required
def professional_profile(request, slug):
    professional = get_object_or_404(Professional, slug=slug, user=request.user)
    return render(request, 'professionals/profile.html', {'professional': professional})
