from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
        
    date = forms.DateField(
    input_formats=['%d.%m.%Y'], 
     )

    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'date', 'ed_info']
        
        
        