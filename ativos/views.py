from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuario.models import Usuarios
from pandas_datareader import data as web
import pandas as pd
import yfinance as yf
from .models import Ativos


def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])
        siglas = Ativos.objects.filter(usuario = usuario)
        '''lmt = yf.Ticker("LMT")
        hist = lmt.history(period="30d",  interval = "60m")
        return HttpResponse(f"olá {usuario} historico da lmt: {hist['Open'], hist['Close']}")'''
        return render(request, 'home.html', {'siglas': siglas})
    else:
        return redirect('/usuario/login/?status=2')
    

def sobre(request):
    return render(request, 'sobre.html')


def user(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])
        return render(request, 'user.html', {'usuario': usuario})
    else:
        return redirect('/usuario/login/?status=2')
    

