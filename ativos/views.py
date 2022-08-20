from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from usuario.models import Usuarios
from yahooquery import Ticker
import yfinance as yf


def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario']).nome
        lmt = yf.Ticker("LMT")
        hist = lmt.history(period="30d",  interval = "60m")
        return HttpResponse(f"olá {usuario} historico da lmt: {hist['Open'], hist['Close']}")
        # return render(request, 'home.html')
    else:
        return redirect('/usuario/login/?status=2')
    

def sobre(request):
    return render(request, 'sobre.html')
    

