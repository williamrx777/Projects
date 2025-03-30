from django import forms

class FormCadastro(forms.Form):
    email = forms.EmailField(max_length=50)
    nome =  forms.CharField(max_length=50)
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

class FormFoto(forms.Form):
    foto = forms.ImageField()