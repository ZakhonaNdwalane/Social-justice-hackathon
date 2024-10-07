from django import forms
from .models import WealthInitiatives

class CreateInitiativeForm(forms.ModelForm):
    class Meta:
        model = WealthInitiatives
        fields = ['initiative_name', 'description', 'funding_goal', 'funds_raised', 'beneficiaries', 'start_date', 'end_date']


