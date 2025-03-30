from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conta(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return '{}'.format(self.foto)