from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto, name='produto'),
]