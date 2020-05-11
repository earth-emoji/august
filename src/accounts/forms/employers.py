from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Employer
from users.models import User


class EmployerSignUpForm(UserCreationForm):
    email = forms.CharField(min_length=1, max_length=60, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    photo = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'inputfile inputfile-custom'}))
    password1 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta(UserCreationForm):
        model = User
        fields = ('name', 'email')

    def save(self):
        user = super().save(commit=False)
        user.save()
        user.is_employer = True
        Employer.objects.create(user=user)
        return user
