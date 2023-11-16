# flights/forms.py
from django import forms
from .models import Flight

class FlightEditForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'duration']
