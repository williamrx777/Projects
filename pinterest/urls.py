from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('perfil/', views.perfil, name='perfil'),
    path('user/<int:usuario_id>', views.user, name='user'),
    path('deletar/', views.deletar, name='deletar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('editar/<int:id>/change', views.editar, name='editar'),
    path('cadastro/', views.cadastroPinterest, name='cadastroPinterest'),
    path('login/',views.loginPinterest, name='loginPinterest'),
    path('sair/', views.sairPinterest, name='sairPinterest'),
]