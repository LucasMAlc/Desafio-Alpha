from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class usuarioAdmin(admin.ModelAdmin):
    readonly_fields= ('nome', 'email', 'senha', 'idade')