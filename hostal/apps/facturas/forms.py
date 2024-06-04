from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    model = Factura
    fields = '__all__'
    widgets = {
            'fecha_emision': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }