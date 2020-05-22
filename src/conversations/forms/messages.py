from django import forms

from conversations.models import Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(max_length=1000, strip=True, widget=forms.TextInput(attrs={}))

    class Meta:
        model = Message
        fields = ['content']