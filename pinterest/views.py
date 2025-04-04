from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.messages import constants
from django.contrib import messages
from .forms import FormCadastro
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,reverse
from .models import Conta
from .forms import FormFoto
from django.contrib.auth.models import User
# Create your views here.

def cadastroPinterest(request):
    if request.method == "GET":
        form = FormCadastro()
        return render(request, 'cadastroPinterest.html',{'form':form})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais.')
    try:
        user = User.objects.create_user(
            username=nome,
            email=email,
            password=senha,
        )
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso.')
        return redirect('loginPinterest')
    except:
        messages.add_message(request, constants.ERROR, 'Tente novamente.')
        return redirect('cadastroPinterest')


def loginPinterest(request):
    if request.method == "GET":
        form = FormCadastro()
        return render(request,'loginPinterest.html',{'form':form})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,
                            password=senha)

        if user is not None:
            login(request, user)
            return redirect('feed')
        if request.user.is_authenticated:
            return redirect('feed')
        else:
            return render(request, 'loginPinterest.html')

def sairPinterest(request):
    logout(request)
    return redirect('loginPinterest')

@login_required
def feed(request):
    if request.method == "GET":
        conta = Conta.objects.all()
        return render(request, 'feed.html',{'foto':conta})
@login_required
def perfil(request):
    if request.method == "GET":
        form = FormFoto()
        conta = Conta.objects.filter(usuario=request.user)
        return render(request, 'perfil.html',{'conta':conta,'form':form})
    elif request.method == "POST":
        foto = request.FILES.get('foto')

        conta = Conta(
            usuario=request.user,
            foto=foto
        )

        conta.save()

        return redirect(reverse('perfil'))

@login_required
def user(request,usuario_id):
    if request.method == "GET":
        user = User.objects.get(pk=usuario_id)
        conta = Conta.objects.filter(usuario=usuario_id)
        return render(request, 'user.html',{'user':user,'conta':conta})

@login_required
def deletar(request):
    if request.method == "GET":
        conta = Conta.objects.filter(usuario=request.user)
        return render(request, 'deletar.html',{'conta':conta})
@login_required
def excluir(request, id):
    conta = Conta.objects.get(id=id)
    if not conta.usuario == request.user:
        return redirect('deletar')
    conta.delete()
    return redirect('deletar')
@login_required
def editar(request, id):
    if request.method == "GET":
        conta = Conta.objects.get(pk=id)
        return render(request,'editar/change.html',{'conta':conta})
    conta = Conta.objects.get(pk=id)
    if request.method == "POST":
        conta.foto = request.FILES.get('foto')

        conta.save()
        return redirect('perfil')