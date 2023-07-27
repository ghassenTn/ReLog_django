# forms.py
# forms.py
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'age']  # Include other fields from the model if needed
        widgets = {
            'useragent': forms.HiddenInput(),  # Render useragent field as hidden input
            'ip': forms.HiddenInput(),         # Render ip field as hidden input
        }

