# Generated by Django 4.1 on 2022-08-30 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ativos', '0007_alter_ativos_intervalo_verificar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativos',
            name='intervalo_verificar',
            field=models.CharField(max_length=20),
        ),
    ]
