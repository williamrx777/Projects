from django import forms
from ramais.models import *
class DepartamentoCadastroForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    nome = forms.CharField(label='Nome', max_length=50,
                           widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite o nome do departamento'}))

class FuncionarioCadastroForm(forms.Form):
      id = forms.IntegerField(required=False, widget=forms.HiddenInput())
      nome = forms.CharField(label='Nome', max_length=50,
                           widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite o nome do funcionario'}))
      ramal = forms.IntegerField(label='Ramal',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Digite o numero do ramal'}))
      email = forms.CharField(label='Email', max_length=50,
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite o E-mail'}))

      departamentoId = forms.ModelChoiceField(label='Departamento', queryset=Departamento.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

class AdministradorCadastroForm(forms.Form):
      id = forms.IntegerField(required=False, widget=forms.HiddenInput())
      nome = forms.CharField(label='Nome' ,max_length=50,
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o nome do funcionario'}))
      ramal = forms.IntegerField(label='Ramal',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Digite o numero do ramal'}))
      email = forms.CharField(label='Email', max_length=50,
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite o E-mail'}))

      ip = forms.CharField(label='Ip', max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite o numero do ip ex:1xx.1xx.2xx.1xx'}))

      departamento = forms.CharField(label='Departamento', max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite o nome do departamento.'}))