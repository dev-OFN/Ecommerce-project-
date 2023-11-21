from django import forms 
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Input password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm password"}))

    class Meta:
        model = User
        fields = ['username', 'email']