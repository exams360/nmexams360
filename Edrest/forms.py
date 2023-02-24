from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Edrest.models import newuser

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})
    )
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=25)
    phone_number = forms.CharField(max_length=10)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = newuser
        fields = ('username', 'phone_number', 'password1', 'password2')