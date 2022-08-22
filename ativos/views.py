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
                print('nenhuma operação recomendada')
                
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

def ver_ativo(request, id):
    if request.session.get('usuario'):
        ativos = Ativos.objects.get(id = id)
        if request.session.get('usuario') == ativos.usuario.id:
            usuario = Usuarios.objects.get(id = request.session['usuario'])
            form = CadastroAtivos()
            form.fields['usuario'].initial = request.session['usuario']

            return render(request, 'ver_ativo.html', {'ativos': ativos,
                                                      'usuario_logado': request.session.get('usuario'),
                                                      'form': form,
                                                      'id_ativo': id})
        else:
            return HttpResponse('ERRO: Ativo não pertence a este usuário')
    return redirect('/usuario/login/?status=2')

def cadastrar_ativo(request):
    if request.method =='POST':
        form = CadastroAtivos(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/home/')
        else:
            return HttpResponse("ERRO: Cadastro inválido")

def excluir_ativo(request, id):
    ativo = Ativos.objects.get(id = id).delete()
    return redirect('/home/') 
      
