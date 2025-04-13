from django.urls import path
from . import adote_views

urlpatterns = [
    path('', adote_views.listar_pets, name="listar_pets"),
    path('pedido_adocao/<int:id_pet>', adote_views.pedido_adocao, name="pedido_adocao"),
    path('processa_pedido_adocao/<int:id_pedido>', adote_views.processa_pedido_adocao, name="processa_pedido_adocao"),
]