from django import forms

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario