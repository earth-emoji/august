from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_employer:
            return redirect('employers:dashboard', request.user.employer.slug)
        elif request.user.is_professional:
            return redirect('jobs:list')
    return render(request, 'pages/home.html')
