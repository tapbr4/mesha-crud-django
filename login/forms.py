from django.forms import ModelForm
from login.models import Usuarios
from django import forms

# Create the form class.
class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['login', 'senha', 'admin']
        widgets = {
            'password': forms.PasswordInput(),
        }
