from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegistrationForm(UserCreationForm):
    first_name=forms.CharField( max_length=30, required=False)
    last_name=forms.CharField( max_length=30, required=False)
    email=forms.EmailField( max_length=30, required=False)


    class Meta:
        model=User
        fields=['first_name','last_name','username',"email",'password1','password2']
 