from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from . models import UserProfile
from .models import *

class PlanUpdateForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['plan']
        labels = {
            'plan': 'Select Plan'
        }
        widgets = {
            'plan': forms.Select(attrs={'class': 'form-control'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Country Code + Phone Number'}))
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class EditUserProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'date_of_birth']
        labels = {
            'phone_number': 'Phone Number',
            'date_of_birth': 'Date of Birth',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = kwargs.get('instance').user if kwargs.get('instance') else None
        if user:
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

class UpdateWithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['wallet_name', 'wallet_address']
        labels = {
            'wallet_name': 'Wallet Name',
            'wallet_address': 'Wallet Address',
        }