from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('home/', views.home, name = 'home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('user/', views.user, name = 'user'),
    path('cadastrar_ativo/', views.cadastrar_ativo, name = 'cadastrar_ativo'),
    path('excluir_ativo/<int:id>', views.excluir_ativo, name = 'excluir_ativo'),
]

