from django.db import models

# Create your models here.

class Lista_Ramais(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    ramal = models.IntegerField()
    departamento = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="example@example.com")
    ip = models.CharField(max_length=100, default="192.168.254.0")

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    ramal = models.IntegerField()
    email = models.CharField(max_length=100, default="example@gmr.com.br")
    departamentoId = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome