# Generated by Django 4.1 on 2022-08-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ativos', '0004_rename_verificar_ativos_intervalo_verificar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativos',
            name='preco_compra',
        ),
        migrations.RemoveField(
            model_name='ativos',
            name='preco_venda',
        ),
        migrations.AlterField(
            model_name='ativos',
            name='intervalo_verificar',
            field=models.IntegerField(default=60),
        ),
    ]
