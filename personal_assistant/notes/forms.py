from django import forms
from .models import Note, Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['body_tag']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control large-input', 
                'style': 'font-size: 1.2rem; height: 50px;'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control large-input', 
                'style': 'font-size: 1.2rem; height: 150px;'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control large-input', 
                'style': 'font-size: 1.2rem; height: 150px;'
            }),
        }

class TagFilterForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        empty_label='All tags',
        label='Filter by tag',
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Filter by tag'})
    )
    search = forms.CharField(
        max_length=30,
        required=False,
        label='Search by title',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by title'})
    )
