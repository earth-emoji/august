from django import forms

from classifications.models import Category
from conversations.models import Room
from conversations.choices import VISIBILITY_CHOICES

class RoomForm(forms.ModelForm):
    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': ''}))
    details = forms.CharField(
        widget=forms.Textarea(attrs={'class': ''}))
    access = forms.CharField(max_length=9, widget=forms.Select(attrs={}, choices=VISIBILITY_CHOICES))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={}))

    class Meta:
        model = Room
        fields = ['name', 'details', 'access', 'category']