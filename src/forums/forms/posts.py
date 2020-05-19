from django import forms

from forums.models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        strip=True, widget=forms.Textarea(attrs={'class ': ''}))

    class Meta:
        model = Post
        fields = ['content']