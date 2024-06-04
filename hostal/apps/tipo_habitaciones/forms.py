from django import forms
from .models import *

class TipoHabitacionForm(forms.ModelForm):
    model = TipoHabitacion
    fields = '__all__'