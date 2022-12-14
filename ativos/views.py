from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuario.models import Usuarios
from pandas_datareader import data as web
import pandas as pd
from .models import Ativos
from datetime import datetime
from .forms import CadastroAtivos
from django.core.mail import send_mail

def inicio(request):
    return redirect('/usuario/login/')

def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])

        ativos = Ativos.objects.filter(usuario = usuario)
        form = CadastroAtivos()
        form.fields['usuario'].initial = request.session['usuario']

        for ativo in ativos:
            try:
                cotacao = web.DataReader(ativo.sigla, data_source='yahoo', start='08/20/2022', end=datetime.now())
                cotacao = pd.DataFrame(cotacao)
                print('valor atual de: ', ativo.sigla, 'é: ', cotacao['Close'].iloc[-1])

                if(cotacao['Close'].iloc[-1] > ativo.preco_venda):
                    send_mail('Ativos', f"Ativo: {ativo.sigla}, Valor: {cotacao['Close'].iloc[-1]}, Ação: Venda",'lucasmoura02@hotmail.com', [f'{usuario.email}'])
                    print('venda', ativo.sigla)

                elif(cotacao['Close'].iloc[-1] < ativo.preco_compra):
                    send_mail('Ativos', f"Ativo: {ativo.sigla}, Valor: {cotacao['Close'].iloc[-1]}, Ação: Compra",'lucasmoura02@hotmail.com', [f'{usuario.email}'])
                    print('compra', ativo.sigla)

                else:
                    print('nenhuma operação recomendada')

            except:
                print("Falha ao obter cotação")

                
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

def editar_ativo(request, id):
    ativos = Ativos.objects.get(id = id)
    form = CadastroAtivos(instance=ativos)
    if request.method =='POST':
        form = CadastroAtivos(request.POST, instance=ativos)
        if form.is_valid():
            form.save()
            return redirect('/home/')
        else:
            return HttpResponse("ERRO: Edição inválida")
    else: 
        return render(request, '/editar_ativo.html', {'form': form, 'ativo': ativos})