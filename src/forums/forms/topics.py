from django import forms

from forums.models import Topic

class TopicForm(forms.ModelForm):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={}))
    description = forms.CharField(widget=forms.Textarea(attrs={}))

    class Meta:
        model = Topic
        fields = ('name', 'description')