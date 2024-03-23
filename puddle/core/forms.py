from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '您的用户名',
        'class' : 'w-full py-4 px-5 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '您的密码',
        'class' : 'w-full py-4 px-5 rounded-xl'
    }))



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '您的用户名',
        'class' : 'w-full py-4 px-5 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': '您的邮箱',
        'class' : 'w-full py-4 px-5 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '您的密码',
        'class' : 'w-full py-4 px-5 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '重复您的密码',
        'class' : 'w-full py-4 px-5 rounded-xl'
    }))
