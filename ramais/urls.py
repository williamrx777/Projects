from django.urls import path
from .admin import *
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('detalhe/', views.administracao, name='administracao'),
   
    # path('funcionarios/<int:id>', views.funcionarios, name='funcionarios'),
    # path('todolist/', views.todolist, name='todolist'),
    path('home/', views.home, name='home'),
    path('cadastroDepartamento/', views.cadastroDepartamento, name='cadastroDepartamento'),
    path('cadastroFuncionario/', views.cadastroFuncionario, name='cadastroFuncionario'),
    path('cadastroAdministrador/', views.cadastroAdministrador, name='cadastroAdministrador'),
    path('listaDepartamento/', views.listaDepartamento, name='listaDepartamento'),
    path('listaFuncionario/', views.listaFuncionario, name='listaFuncionario'),
    path('listaAdministrador/', views.listaAdministrador, name='listaAdministrador'),
    # path('buscar/', views.buscar, name='buscar'),
    path('cadastrarDepartamento/', views.cadastrarDepartamento, name='cadastrarDepartamento'),
    path('cadastrarFuncionario/', views.cadastrarFuncionario, name='cadastrarFuncionario'),
    path('cadastrarAdministrador/', views.cadastrarAdministrador, name='cadastrarAdministrador'),
    path('excluirDepartamento/<int:id>', views.excluirDepartamento, name='excluirDepartamento'),
    path('excluirFuncionario/<int:id>', views.excluirFuncionario, name='excluirFuncionario'),
    path('excluirAdministrador/<int:id>', views.excluirAdministrador, name='excluirAdministrador'),
    path('alterarDepartamento/<int:id>', views.alterarDepartamento, name='alterarDepartamento'),
    path('alterarFuncionario/<int:id>', views.alterarFuncionario, name='alterarFuncionario'),
    path('alterarAdministrador/<int:id>', views.alterarAdministrador, name='alterarAdministrador'),
    path('login/', views.logar, name='logar'),
    path('sair/', views.sair, name='sair'),
]