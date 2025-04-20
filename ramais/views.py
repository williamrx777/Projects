from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.db.models import F
from django.contrib.auth.models import User
# Create your views here.

def lista(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        
        departamentos = Departamento.objects.all()
        ramais = Funcionario.objects.all()
        if nome:
            departamentos = departamentos.filter(nome__icontains=nome)
           
            ramais = ramais.filter(nome__icontains=nome)
        else:
            departamentos = Departamento.objects.all()
            ramais = Funcionario.objects.all()
        return render(request, 'index.html', {'ramais': ramais, 'nome':nome, 'departamentos': departamentos})

@login_required
def administracao(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        ramal = request.GET.get('ramal')
        ip = request.GET.get('ip')
        if nome:
            ramais = Lista_Ramais.objects.filter(nome__icontains=nome)
        elif ramal:
             ramais = Lista_Ramais.objects.filter(ramal__icontains=ramal)
        # elif ip:
        #     ramais = Lista_Ramais.objects.filter(ip__icontains=ip)
        else:
           ramais = Lista_Ramais.objects.all()
        return render(request, 'administracao.html', {'ramais': ramais,'ramal':ramal,'ip':ip, 'nome':nome})    

# def funcionarios(request, id):
#     if request.method == "GET":
#         nome = request.GET.get('nome')
#         departamento = Departamento.objects.filter(id=id).first()
#         ramais = Funcionario.objects.filter(departamentoId=id)
#         return render(request, 'funcionarios.html', {'ramais': ramais, 'nome': nome, 'departamento': departamento})

# def todolist(request):
#     return render(request, 'todolist.html')

@login_required
def principal(request):
    return render(request,'principal.html')
@login_required
def cadastroDepartamento(request):

    formDepartamento = DepartamentoCadastroForm()

    return render(request, 'cadastroDepartamento.html',{'formDepartamento':formDepartamento})
@login_required
def cadastroFuncionario(request):

    formFuncionario = FuncionarioCadastroForm()

    return render(request, 'cadastroFuncionario.html',{'formFuncionario':formFuncionario})
@login_required
def cadastroAdministrador(request):

    formAdministrador = AdministradorCadastroForm()

    return render(request, 'cadastroAdministrador.html',{'formAdministrador':formAdministrador})
    pass
@login_required
def listaDepartamento(request: HttpRequest):
    if request.method == "GET":
        nome = request.GET.get('nome')
        ordenacao = request.GET.get('ordenacao')
        departamento = Departamento.objects.all()

        if nome:
            departamento = departamento.filter(nome__icontains=nome)

        # Definindo o estado padrão de ordenação
        ordenacao_estado = 'asc'

        # Definindo a ordenação padrão para o campo 'id'
        ordenacao_campo = 'id'

        # Verificando se um campo de ordenação específico foi fornecido
        if ordenacao:
            if ordenacao.startswith('-'):
                ordenacao_estado = 'desc'
                ordenacao_campo = ordenacao[1:]  # Removendo o prefixo '-' para obter o nome do campo
            else:
                ordenacao_estado = 'asc'
                ordenacao_campo = ordenacao

        # Aplicando a ordenação para o campo especificado
        if ordenacao_campo == 'id':
            departamento = departamento.order_by(F('id').asc() if ordenacao_estado == 'asc' else F('id').desc())

        else:
            departamento = departamento.order_by(F('nome').asc() if ordenacao_estado == 'asc' else F('nome').desc())

        return render(request, 'listaDepartamento.html', {'departamento': departamento, 'ordenacao_estado': ordenacao_estado})
@login_required
def listaAdministrador(request):
     if request.method == "GET":
        nome = request.GET.get('nome')
        ordenacao = request.GET.get('ordenacao')

        administrador = Lista_Ramais.objects.all()

        if nome:
            administrador = administrador.filter(nome__icontains=nome)

        # Definindo o estado padrão de ordenação
        ordenacao_estado = 'asc'

        # Definindo a ordenação padrão para o campo 'id'
        ordenacao_campo = 'id'

        # Verificando se um campo de ordenação específico foi fornecido
        if ordenacao:
            if ordenacao.startswith('-'):
                ordenacao_estado = 'desc'
                ordenacao_campo = ordenacao[1:]  # Removendo o prefixo '-' para obter o nome do campo
            else:
                ordenacao_estado = 'asc'
                ordenacao_campo = ordenacao

        # Aplicando a ordenação para o campo especificado
        if ordenacao_campo == 'id':
            administrador = administrador.order_by(F('id').asc() if ordenacao_estado == 'asc' else F('id').desc())
        elif ordenacao_campo == 'ramal':
            administrador = administrador.order_by(F('ramal').asc() if ordenacao_estado == 'asc' else F('ramal').desc())
        elif ordenacao_campo == 'email':
            administrador = administrador.order_by(F('email').asc() if ordenacao_estado == 'asc' else F('email').desc())
        elif ordenacao_campo == 'ip':
            administrador = administrador.order_by(F('ip').asc() if ordenacao_estado == 'asc' else F('ip').desc())
        elif ordenacao_campo == 'departamento':
            administrador = administrador.order_by(F('departamento').asc() if ordenacao_estado == 'asc' else F('departamento').desc())
        else:
            administrador = administrador.order_by(F('nome').asc() if ordenacao_estado == 'asc' else F('nome').desc())

        return render(request, 'listaAdministrador.html', {'administrador': administrador, 'ordenacao_estado': ordenacao_estado})

@login_required
def listaFuncionario(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        ordenacao = request.GET.get('ordenacao')

        funcionario = Funcionario.objects.all()

        if nome:
            funcionario = funcionario.filter(nome__icontains=nome)

        # Definindo o estado padrão de ordenação
        ordenacao_estado = 'asc'

        # Definindo a ordenação padrão para o campo 'id'
        ordenacao_campo = 'id'

        # Verificando se um campo de ordenação específico foi fornecido
        if ordenacao:
            if ordenacao.startswith('-'):
                ordenacao_estado = 'desc'
                ordenacao_campo = ordenacao[1:]  # Removendo o prefixo '-' para obter o nome do campo
            else:
                ordenacao_estado = 'asc'
                ordenacao_campo = ordenacao

        # Aplicando a ordenação para o campo especificado
        if ordenacao_campo == 'id':
            funcionario = funcionario.order_by(F('id').asc() if ordenacao_estado == 'asc' else F('id').desc())
        elif ordenacao_campo == 'ramal':
            funcionario = funcionario.order_by(F('ramal').asc() if ordenacao_estado == 'asc' else F('ramal').desc())
        elif ordenacao_campo == 'email':
            funcionario = funcionario.order_by(F('email').asc() if ordenacao_estado == 'asc' else F('email').desc())
        elif ordenacao_campo == 'departamentoId':
            funcionario = funcionario.order_by(F('departamentoId').asc() if ordenacao_estado == 'asc' else F('departamentoId').desc())
        else:
            funcionario = funcionario.order_by(F('nome').asc() if ordenacao_estado == 'asc' else F('nome').desc())

        return render(request, 'listaFuncionario.html', {'funcionario': funcionario, 'ordenacao_estado': ordenacao_estado})


@login_required
def cadastrarDepartamento(request):
    try:
        if request.method == 'POST':
            formDepartamento = DepartamentoCadastroForm(request.POST)
            if formDepartamento.is_valid():
                departamento = Departamento()
                departamento.nome = formDepartamento.cleaned_data['nome']
                msg = 'Departamento Cadastrado com sucesso.'
                if formDepartamento.cleaned_data['id'] is not None:
                    departamento.id = formDepartamento.cleaned_data['id']
                    msg = 'Departamento alterado com sucesso.'
                departamento.save()
                return render(request, 'cadastroDepartamento.html',{'msg':msg,'formDepartamento':DepartamentoCadastroForm()})
            else:
                raise Exception('%s, FormErrors' % formDepartamento.errors)
        else:
            raise Exception('Use POST para formularios, MethodEnvioError')
    except Exception as ex:
        msg = ex.args
        return render(request, 'cadastroDepartamento.html',{'msg':msg,'form':DepartamentoCadastroForm()})
@login_required
def cadastrarFuncionario(request):
    try:
        if request.method == 'POST':
            formFuncionario = FuncionarioCadastroForm(request.POST)
            if formFuncionario.is_valid():
                funcionario = Funcionario()
                funcionario.nome = formFuncionario.cleaned_data['nome']
                funcionario.ramal = formFuncionario.cleaned_data['ramal']
                funcionario.email = formFuncionario.cleaned_data['email']
                funcionario.departamentoId = formFuncionario.cleaned_data['departamentoId']
                msg = 'Funcionario cadastrado com sucesso.'
                if formFuncionario.cleaned_data['id'] is not None:
                    funcionario.id = formFuncionario.cleaned_data['id']
                    msg = 'Funcionario alterado com sucesso.'
                funcionario.save()
                return render(request, 'cadastroFuncionario.html', {'msg':msg,'formFuncionario':FuncionarioCadastroForm()})
            else:
                raise Exception('%s, FormErrors' % formFuncionario.errors)
        else:
            raise Exception('Use POST para formularios, MethodEnvioError')
    except Exception as ex:
        msg = ex. args
        return render(request, 'cadastroFuncionario.html',{'msg':msg,'form':FuncionarioCadastroForm()})
@login_required
def cadastrarAdministrador(request):
    try:
        if request.method == 'POST':
            formAdministrador = AdministradorCadastroForm(request.POST)
            if formAdministrador.is_valid():
                funcionario = Lista_Ramais()
                funcionario.nome = formAdministrador.cleaned_data['nome']
                funcionario.ramal = formAdministrador.cleaned_data['ramal']
                funcionario.email = formAdministrador.cleaned_data['email']
                funcionario.ip = formAdministrador.cleaned_data['ip']
                funcionario.departamento = formAdministrador.cleaned_data['departamento']
                msg = 'Funcionario cadastrado com sucesso.'
                if formAdministrador.cleaned_data['id'] is not None:
                    funcionario.id = formAdministrador.cleaned_data['id']
                    msg = 'Funcionario alterado com sucesso.'
                funcionario.save()
                return render(request, 'cadastroAdministrador.html', {'msg':msg,'formAdministrador':AdministradorCadastroForm()})
            else:
                raise Exception('%s, FormErrors' % formAdministrador.errors)
        else:
            raise Exception('Use POST para formularios, MethodEnvioError')
    except Exception as ex:
        msg = ex. args
        return render(request, 'cadastroAdministror.html',{'msg':msg,'form':AdministradorCadastroForm()})
@login_required
def excluirDepartamento(request, id):
    try:
        departamento = Departamento.objects.get(pk=id)

        resultDepartamento = departamento.delete()

        if resultDepartamento[0] > 0:
            msg = 'Departamento deletado com sucesso.'
        else:
            msg = 'Nenhum Departamento ou Funcionario encontrado!'

        return render(request, 'listaDepartamento.html',{'departamento':Departamento.objects.all(),'msg':msg})

    except Exception as ex:
        msg = ex.args
        return render(request, 'listaDepartamento.html',{'msg':msg,'departamento':Departamento.objects.all()})
@login_required
def excluirFuncionario(request, id):
    try:

        funcionario = Funcionario.objects.get(pk=id)

        resultFuncionario = funcionario.delete()

        if resultFuncionario[0] > 0:
            msg = 'Funcionario deletado com sucesso'
        else:
            msg = 'Nenhum Departamento ou Funcionario encontrado!'

        return render(request, 'listaFuncionario.html',{'funcionario':Funcionario.objects.all(),'msg':msg})
    except Exception as ex:
        msg = ex.args
        return render(request, 'listaFuncionario.html',{'msg':msg,'funcionario':Funcionario.objects.all()})
@login_required
def excluirAdministrador(request,id):
    try:

        administrador = Lista_Ramais.objects.get(pk=id)

        resultAdministrador = administrador.delete()

        if resultAdministrador[0] > 0:
            msg = 'Funcionario deletado com sucesso'
        else:
            msg = 'Nenhum Funcionario encontrado!'

        return render(request, 'listaAdministrador.html',{'administrador':Lista_Ramais.objects.all(),'msg':msg})
    except Exception as ex:
        msg = ex.args
        return render(request, 'listaAdministrador.html',{'msg':msg,'administrador':Lista_Ramais.objects.all()})
    pass

@login_required
def alterarDepartamento(request, id):
    try:
        departamento = Departamento.objects.get(pk=id)

        formDepartamento = DepartamentoCadastroForm(
            initial={
                'id': departamento.id,
                'nome':departamento.nome,
            })

        return render(request, 'cadastroDepartamento.html',{'formDepartamento':formDepartamento})
    except Exception as ex:
        msg = ex.args
        return render(request, 'lista.html',{'msg':msg, 'departamento':Departamento.objects.all()})
@login_required
def alterarFuncionario(request,id):
    try:
        funcionario = Funcionario.objects.get(pk=id)

        formFuncionario = FuncionarioCadastroForm(
            initial={
                'id':funcionario.id,
                'nome':funcionario.nome,
                'ramal':funcionario.ramal,
                'email':funcionario.email,
                'departamentoId':funcionario.departamentoId
            })
        return render(request, 'cadastroFuncionario.html',{'formFuncionario':formFuncionario})
    except Exception as ex:
        msg = ex.args
        return render(request, 'lista.html',{'msg':msg, 'funcionario':Funcionario.objects.all()})
@login_required
def alterarAdministrador(request,id):
    try:
        administrador = Lista_Ramais.objects.get(pk=id)

        formAdministrador = AdministradorCadastroForm(
            initial={
                'id':administrador.id,
                'nome':administrador.nome,
                'ramal':administrador.ramal,
                'email':administrador.email,
                'ip':administrador.ip,
                'departamento':administrador.departamento
            })
        return render(request, 'cadastroAdministrador.html',{'formAdministrador':formAdministrador})
    except Exception as ex:
        msg = ex.args
        return render(request, 'cadastroAdministrador.html',{'msg':msg, 'administrador':Lista_Ramais.objects.all()})
    pass

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/ramais/')
        if request.user.is_authenticated:
            return redirect('/ramais/')
        else:
            msg = 'Usuario ou senha incorreto.'
            return render(request, 'login.html', {'msg':msg})
    pass

def sair(request):
    logout(request)
    return redirect('/ramais/login/')
    pass