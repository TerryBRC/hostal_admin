from django import forms
from .models import SysConfig

class ConfigForm(forms.ModelForm):
    class Meta:
        model = SysConfig
        fields = [{'claver','valor'}]