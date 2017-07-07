from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, DateField
from Fisiorganizer_SITE.models import Customer, Session, Exercise
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {
            'username': 'Usuário',
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = "__all__"
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }

        labels = {
            'id_instructor': 'Professor',
            'id_customer': 'Aluno',
            'date': 'Data',
            'time': 'Hora'
        }

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"

