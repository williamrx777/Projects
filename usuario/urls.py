from django.urls import path
from . import adote_views

urlpatterns = [
    path('cadastro/', adote_views.adote_cadastro, name='adote_cadastro'),
    path('logar/', adote_views.adote_login, name="adote_login"),
    path('sair/', adote_views.adote_sair, name="adote_sair"),
]