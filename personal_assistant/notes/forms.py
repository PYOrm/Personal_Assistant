from django import forms
from .models import Note, Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['body_tag']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['body', 'tags']
        widgets = {
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'})  
        }

class TagFilterForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        empty_label='All tags',
        label='Filter by tag',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
