from django import forms

from jobs.models import WorkHistory, EducationHistory, Reference
from jobs.choices import KNOWN_MEASURE_CHOICES, REFERENCE_TYPE_CHOICES

class WorkHistoryForm(forms.ModelForm):
    employer_name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={}))
    job_title = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={}))
    duties = forms.CharField(
        widget=forms.Textarea(attrs={}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = WorkHistory
        fields = ['employer_name', 'start_date', 'end_date', 'job_title', 'duties']

class EducationHistoryForm(forms.ModelForm):
    school_name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={}))
    certificate = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={}))
    did_complete = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hidden', 'tabindex': '0'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = EducationHistory
        fields = ['school_name', 'start_date', 'end_date', 'certificate', 'did_complete']

class ReferenceForm(forms.ModelForm):
    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={}))
    contact_info = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={}))
    known_span = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'placeholder':'Enter the number'}))
    known_measure = forms.CharField(max_length=15, widget=forms.Select(attrs={}, choices=KNOWN_MEASURE_CHOICES))
    reference_type = forms.CharField(max_length=15, widget=forms.Select(attrs={'class':''}, choices=REFERENCE_TYPE_CHOICES))
    
    class Meta:
        model = Reference
        fields = ['name', 'known_span', 'known_measure', 'contact_info', 'reference_type']