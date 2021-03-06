# Generated by Django 3.1.2 on 2021-05-16 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0002_auto_20210515_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='estatus',
            field=models.CharField(choices=[('A', 'Aprobado'), ('B', 'No Aprobado'), ('C', 'No Evaluado')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='fechaEntrevista',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 14, 56, 41, 671122)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='fechaRegistro',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 14, 56, 41, 670127)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='puntuacion',
            field=models.IntegerField(default=0),
        ),
    ]
