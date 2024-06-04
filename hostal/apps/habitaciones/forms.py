from django import forms
from .models import Habitacion

class HabitacionForm(forms.ModelForm):
    model = Habitacion
    fields = '__all__'