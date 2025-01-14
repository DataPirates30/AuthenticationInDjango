from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(empty_value=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


