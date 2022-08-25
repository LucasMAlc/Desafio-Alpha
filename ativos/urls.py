from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('home/', views.home, name = 'home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('user/', views.user, name = 'user'),
    path('ver_ativo/<int:id>', views.ver_ativo, name ='ver_ativo'),
    path('cadastrar_ativo/', views.cadastrar_ativo, name = 'cadastrar_ativo'),
    path('excluir_ativo/<int:id>', views.excluir_ativo, name = 'excluir_ativo'),
    path('editar_ativo/<int:id>', views.editar_ativo, name = 'editar_ativo'),
]

