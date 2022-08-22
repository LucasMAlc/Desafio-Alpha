from hmac import compare_digest
from tracemalloc import start
from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuario.models import Usuarios
from pandas_datareader import data as web
import pandas as pd
from .models import Ativos
from datetime import datetime
from .forms import CadastroAtivos

def inicio(request):
    return redirect('/usuario/login/')

def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])

        ativos = Ativos.objects.filter(usuario = usuario)
        form = CadastroAtivos()
        form.fields['usuario'].initial = request.session['usuario']

        for ativo in ativos:
            x = web.DataReader(ativo.sigla, data_source='yahoo', start='08/19/2022', end=datetime.now())
            x = pd.DataFrame(x)
            print('valor atual de: ', ativo.sigla, 'é: ', x['Close'])
            if(x['Close'].iloc[0] > ativo.preco_venda):
                print('vende', ativo.sigla)

            elif(x['Close'].iloc[0] < ativo.preco_compra):
                print('compra', ativo.sigla)
            else:
                print('valor igual')
                


        return render(request, 'home.html', {'ativos': ativos,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form,
                                             })

    else:
        return redirect('/usuario/login/?status=2')
    

def sobre(request):
    return render(request, 'sobre.html', {'usuario_logado': request.session.get('usuario')})


def user(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])
        return render(request, 'user.html', {'usuario': usuario, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/usuario/login/?status=2')

def cadastrar_ativo(request):
    if request.method =='POST':
        form = CadastroAtivos(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/home/')
        else:
            return HttpResponse("dados inválidos")

def excluir_ativo(request):
    return HttpResponse('excluido')     
