from django import forms
from .models import WealthInitiatives
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateInitiativeForm(forms.ModelForm):
    class Meta:
        model = WealthInitiatives
        fields = ['initiative_name', 'description', 'funding_goal', 'funds_raised', 'beneficiaries', 'start_date', 'end_date']

class contactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class userCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  