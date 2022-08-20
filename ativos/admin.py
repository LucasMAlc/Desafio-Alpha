from django.contrib import admin
from .models import Ativos

@admin.register(Ativos)
class ativosAdmin(admin.ModelAdmin):
    readonly_fields= ('sigla', 'usuario')