from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('user/', views.user, name = 'user'),
]
