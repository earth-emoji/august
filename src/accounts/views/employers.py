from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView

from users.decorators import employer_required
from accounts.forms.employers import EmployerSignUpForm
from accounts.models import Employer
from users.models import User

class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('employers:dashboard', user.slug)

@login_required
@employer_required
def employer_dashboard(request, slug):
    employer = get_object_or_404(Employer, slug=slug, user=request.user)
    return render(request, 'employers/dashboard.html', {'employer': employer})
