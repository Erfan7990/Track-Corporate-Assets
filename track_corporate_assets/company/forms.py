from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

# Import Models
from .models import *

# Create your models here.
class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}), label='Company Name')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Confirm Password'}))
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'address', 'password1', 'password2']
        
        

class DevicesForm(forms.ModelForm):
    
    class Meta:
        model = Device
        fields = ('__all__')
        exclude = ('user','slug')
        widgets = {
            'name': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Device Name'}),
            'price': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        }