from django.shortcuts import render
from .models import Produto
# Create your views here.

def produto(request):
    produtos = Produto.objects.all().order_by('-data_cadastro')  # opcional: limitar com [:12]
    return render(request, 'produto.html', {produtos: produtos})