from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'usuario'}), max_length=150, required=True, help_text='Requerido. Máximo 150 caracteres. Solo letras, números y @ /. / + / - / _.')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email'}), max_length=254, required=True, help_text='Se requiere una direccion de email valida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )