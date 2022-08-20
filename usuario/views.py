from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuarios
from hashlib import sha256

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    idade = request.POST.get('idade')

    usuario = Usuarios.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('cadastro/?status=1')
    
    if len(senha) < 6:
        return redirect('cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuarios(nome = nome, email = email, senha = senha, idade = idade)
        usuario.save()

        return redirect('cadastro/?status=0')
    except:
        return redirect('cadastro/?status=4')
