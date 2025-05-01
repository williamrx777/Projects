from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    estoque = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome