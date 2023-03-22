from django import forms
from .models import DkaData
from .models import SavedData

class DkaForm(forms.ModelForm):
    class Meta:
        model = DkaData
        exclude = ('id',)
        
class SavedForm(forms.ModelForm):
    class Meta:
        model = SavedData
        exclude = ('id',)
