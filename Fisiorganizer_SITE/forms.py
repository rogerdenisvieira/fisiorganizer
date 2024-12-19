from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, DateField, ValidationError
from Fisiorganizer_SITE.models import Patient, Evolution, Place, Session
import datetime

from Fisiorganizer_SITE.validators import validate_phone


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


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

        labels = {
            'name' : 'Nome Completo',
            'address' : 'Endereço',
            'city' : 'Cidade',
            'phone' : 'Telefone',
            'cellphone':'Celular',
            'birthday':'Data de Nascimento',
            'details':'Detalhes'
        }

        widgets = {
            'birthday': DateInput()
        }


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = "__all__"
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }

        labels = {
            'instructor': 'Profissional',
            'customer': 'Aluno',
            'modality': 'Modalidade',
            'date': 'Data',
            'time': 'Hora'
        }

class EvolutionForm(ModelForm):
    class Meta:
        model = Evolution
        fields = "__all__"
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }

        labels = {
            'instructor': 'Profissional',
            'customer': 'Paciente',
            'modality': 'Modalidade',
            'place': 'Local',
            'description_before': 'Condição Inicial',
            'description_after': 'Condição Final',
            'date': 'Data',
            'time': 'Hora'
        }

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        labels = {
            'name': 'Nome',
            'address': 'Endereço',
            'city': 'Cidade',
            'phone': 'Telefone',
            'details': 'Detalhes'
        }

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
        
    #     if validate_phone(phone):
    #         raise ValidationError(f'{phone} não é um número de telefone válido')