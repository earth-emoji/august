from django import forms

# from jobs.models import Application, Job


class ApplicationForm(forms.Form):
    interest = forms.CharField(
        widget=forms.Textarea(attrs={}))
    skills = forms.MultipleChoiceField(
        label='Skills', choices=[], widget=forms.CheckboxSelectMultiple(attrs={}))

    def __init__(self, skills, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        #skills = kwargs.pop('skills')
        self.fields['skills'].choices = skills
