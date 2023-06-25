from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class FormularioUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','last_name','email', 'password1', 'password2']


class FormularioLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']