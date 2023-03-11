from django import forms
from .models import *
from company.models import *

class EmployeeModelForm(forms.ModelForm):
    # device =  forms.MultipleChoiceField()
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}), label='Name')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}))
    given_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input','placeholder': 'yyyy-mm-dd'}))
    return_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'yyyy-mm-dd'}))
    # is_paid = forms.BooleanField()
    
    class Meta:
        model = Employee
        fields = ('__all__')
        exclude = ('user','is_paid',)

class DeviceFeedBackForm(forms.ModelForm):
    
    class Meta:
        model = Device_Feedback
        fields = ('__all__')
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('__all__')