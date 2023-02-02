from django import forms
from .models import Setting

class SettingForm(forms.ModelForm):
    
    class Meta:
        model = Setting
        fields = ('api_key', 'secret_key')
