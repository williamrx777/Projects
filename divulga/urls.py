from django.urls import path
from . import adote_views

urlpatterns = [
    path('novo_pet/', adote_views.novo_pet, name="novo_pet"),
    path('seus_pets/', adote_views.seus_pets, name="seus_pets"),
    path('remover_pet/<int:id>', adote_views.remover_pet, name="remover_pet"),
    path('ver_pet/<int:id>', adote_views.ver_pet, name="ver_pet"),
    path('ver_pedido_adocao/', adote_views.ver_pedido_adocao, name="ver_pedido_adocao"),
    path('dashboard/', adote_views.dashboard, name="dashboard"),
    path('api_adocoes_por_raca/', adote_views.api_adocoes_por_raca, name="api_adocoes_por_raca"),
]