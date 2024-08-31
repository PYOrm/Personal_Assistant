from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control', 'placeholder': 'ДД.ММ.РРРР'}),
        input_formats=['%d.%m.%Y']
    )
    
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'date', 'ed_info']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'ed_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
       