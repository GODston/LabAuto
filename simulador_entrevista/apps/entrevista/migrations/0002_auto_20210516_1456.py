# Generated by Django 3.1.2 on 2021-05-16 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrevista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestaentrevista',
            name='puntuacion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='fechaActualizacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 14, 56, 41, 672121)),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 14, 56, 41, 672121)),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='preguntas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fechaActualizacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 14, 56, 41, 673116)),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 14, 56, 41, 673116)),
        ),
    ]
