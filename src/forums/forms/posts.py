from django import forms
from tinymce import TinyMCE
from forums.models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={
            'required': True,
        }))

    class Meta:
        model = Post
        fields = ['content']