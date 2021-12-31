from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=15, widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})))
    first_name = forms.CharField(max_length=15, widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'})))
    last_name = forms.CharField(max_length=15, widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lastname'})))
    password1 = forms.CharField(max_length=20, label="Password", widget=(
        forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})))
    password2 = forms.CharField(max_length=20, label="Confirm-Password", widget=(
        forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})))
    email = forms.CharField(max_length=100,
                            widget=(
                                forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = '__all__'
