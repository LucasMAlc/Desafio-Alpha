from django.contrib import admin
from .models import Ativos

admin.site.register(Ativos)

''' 
Somente para leitura no admin:

@admin.register(Ativos)
class ativosAdmin(admin.ModelAdmin):
    readonly_fields= ('sigla', 'usuario')

'''