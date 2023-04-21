from django import forms
from AppCoder.models import UserCreationForm

class UserCreationForm(forms.Form):
    
     username=forms.CharField(max_length=30)
     password=forms.CharField(max_length=30)
     email=forms.EmailField()