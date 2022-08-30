from __future__ import absolute_import
from celery import shared_task
from .models import Ativos
from usuario.models import Usuarios
from pandas_datareader import data as web
import pandas as pd
from datetime import datetime
from django.core.mail import send_mail

from celery.schedules import crontab

@shared_task
def enviar_email(id):
        usuario = Usuarios.objects.get(id = id)

        ativos = Ativos.objects.filter(usuario = usuario)

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
