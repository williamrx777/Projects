from django.shortcuts import render
from .models import *
# Create your views here.

def produto(request):
    produto = Produto.objects.all()
    return render(request, 'produto.html', {produto: produto})