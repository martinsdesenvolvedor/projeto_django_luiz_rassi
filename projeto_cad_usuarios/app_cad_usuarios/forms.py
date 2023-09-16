from django import forms

class FormularioCadastroUsuario(forms.Form):
    nome = forms.CharField(max_length=100)
    idade = forms.CharField(max_length=3)
    email = forms.EmailField(max_length=100)
    telefone = forms.CharField(max_length=13)