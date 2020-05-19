from django.contrib.postgres.forms import SimpleArrayField
from django import forms

from jobs.models import Job

class JobForm(forms.ModelForm):

    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-pill'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    positions_to_fill = forms.IntegerField(min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control rounded-pill'}))
    skills = SimpleArrayField(forms.CharField(max_length=2000), widget=forms.Textarea())

    class Meta:
        model = Job
        fields = ('name', 'description', 'positions_to_fill', 'skills')
