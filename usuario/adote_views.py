from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.

def adote_cadastro(request):
    if request.method == "GET":
        return render(request, 'adoteCadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.WARNING, 'Preencha todos os campos')
            return render(request, 'adoteCadastro.html')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais')
            return render(request, 'adoteCadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
            return render(request, 'adoteCadastro.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno')
            return render(request, 'adoteCadastro.html')

def adote_login(request):
    if request.method == "GET":
        return render(request, 'adoteLogin.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,
                      password=senha)

    if user is not None:
      login(request, user)
      return redirect('/adote/divulga/novo_pet')
    if request.user.is_authenticated:
        return redirect('/adote/divulga/novo_pet')
    else:
      messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
      return render(request, 'adoteLogin.html')    

def adote_sair(request):
    logout(request)
    return redirect('/adote/usuario/logar/')