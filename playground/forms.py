from django import forms
from .models import DkaData

class DkaForm(forms.ModelForm):
    class Meta:
        model = DkaData
        exclude = ('id',)
