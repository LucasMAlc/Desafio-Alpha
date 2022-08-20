from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length= 100)
    senha = models.CharField(max_length=30)
    email = models.EmailField (max_length= 200)
    idade = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'

    def __str__(self):
        return self.nome