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
            'tag': forms.CheckboxSelectMultiple()    
        }