from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {
            'username': ('Usuário'),
        }