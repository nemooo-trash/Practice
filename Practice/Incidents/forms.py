from django import forms

from .models import *

class AddIncidentForm(forms.ModelForm):
    class Meta:
        model = Incidents
        fields = ('address', 'description', 'latitude', 'longitude', 'taken_measures')
        widgets = {
            'latitude': forms.TextInput(attrs={'readonly': 'readonly'}),
            'longitude': forms.TextInput(attrs={'readonly': 'readonly'}),
        }




