from django import forms
from .models import Stable

class StableForm(forms.ModelForm):
    class Meta:
        model = Stable
        fields = ['name', 'address', 'capacity']
    