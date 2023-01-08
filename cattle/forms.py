from django import forms
from .models import Cattle
from stable.models import Stable

class CattleForm(forms.ModelForm):
    class Meta:
        model = Cattle
        fields = ['weight', 'stable']
    
    stable = forms.ModelChoiceField(queryset=Stable.objects.all())
