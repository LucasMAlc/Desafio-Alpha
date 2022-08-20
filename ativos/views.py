from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from usuario.models import Usuarios

def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario']).nome
        return HttpResponse(f'olá {usuario}')
        # return render(request, 'home.html')
    else:
        return redirect('/usuario/login/?status=2')
    

def sobre(request):
    return render(request, 'sobre.html')
    

