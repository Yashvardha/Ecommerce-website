from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','state','zipcode']


