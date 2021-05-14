# Generated by Django 3.2 on 2021-05-04 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appEmpresa', '0001_initial'),
        ('appCandidato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestaEntrevista',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('puntuacion', models.IntegerField()),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCandidato.candidato', verbose_name='Relacion de respuestas con candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=255)),
                ('preguntas', models.IntegerField()),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField()),
                ('vacante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEmpresa.vacante', verbose_name='Relacion de la entrevista con la vacante')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('respuesta', models.TextField()),
                ('contesta_entrevista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrevista.contestaentrevista', verbose_name='Relacion con contestacion entrevistado')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField()),
                ('entrevista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrevista.entrevista', verbose_name='Relacion de la pregunta con la entrevista')),
            ],
        ),
        migrations.CreateModel(
            name='Grabacion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('archivo', models.CharField(max_length=255)),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrevista.respuesta', verbose_name='Relacion con la respuesta del candidato')),
            ],
        ),
        migrations.AddField(
            model_name='contestaentrevista',
            name='entrevista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEntrevista.entrevista', verbose_name='Relacion de respuestas con la entrevista'),
        ),
    ]