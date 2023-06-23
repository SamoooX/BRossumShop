from django import forms
from .models import Usuario
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

# class CustomerUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password1', 'password2']