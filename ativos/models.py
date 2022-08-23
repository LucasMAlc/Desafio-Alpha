from django.db import models
from usuario.models import Usuarios

class Ativos(models.Model):
    sigla = models.CharField(max_length= 100)
    preco_compra = models.IntegerField(blank=True, null=True)
    preco_venda = models.IntegerField(blank=True, null=True)
    intervalo_verificar = models.CharField(max_length=10)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Ativo'

    def __str__(self):
        return self.sigla 


