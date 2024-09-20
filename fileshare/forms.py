from django import forms
from .models import File

class FileUploadForm(forms.Form):
    file = forms.FileField(required=True)
    category = forms.ChoiceField(choices=File.CATEGORY_CHOICES, required=True)


