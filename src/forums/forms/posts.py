from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from forums.models import Post

class PostForm(forms.Form):
    content = SummernoteTextFormField(widget=SummernoteInplaceWidget())
