from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    model = Reserva
    fields = '__all__'
    widgets = {
            'fecha_entrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }