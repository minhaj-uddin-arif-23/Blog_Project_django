from django import forms 
from . models import ProFile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProFile
        fields ="__all__"
       