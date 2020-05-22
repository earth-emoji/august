from django import forms
from mdeditor.fields import MDTextFormField

from conversations.models import Message

class MessageForm(forms.Form):
    content = MDTextFormField()