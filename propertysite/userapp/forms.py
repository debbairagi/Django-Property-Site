from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from userapp.models import Agent

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1' , 'password2']

# Login in a UserUser
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
class CreateAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name','last_name','email','phone_number','address','city','state','zipcode','biography',]

