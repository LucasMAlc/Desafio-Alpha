from django.contrib import admin
from .models import Ativos

''' 
Para editar no admin:
admin.site.register(Ativos)

Somente para leitura no admin:
'''
@admin.register(Ativos)
class ativosAdmin(admin.ModelAdmin):
    readonly_fields= ('sigla', 'preco_compra', 'preco_venda', 'intervalo_verificar', 'usuario')

