from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuarios
from hashlib import sha256

def cadastro(request):
    status = request.GET.get('status') 
    return render(request, 'cadastro.html', {'status': status})

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

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

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuarios.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f"/home/?id_usuario={request.session['usuario']}")

    return HttpResponse(f'{email} {senha}')

def sair(request):
    request.session.flush()
    return redirect('/usuario/login/')