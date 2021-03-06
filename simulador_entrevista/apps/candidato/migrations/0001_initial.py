# Generated by Django 3.2 on 2021-05-15 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
        ('empresa', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=255)),
                ('puntuacion', models.IntegerField()),
                ('estatus', models.CharField(choices=[('A', 'Aprobado'), ('B', 'No Aprobado'), ('C', 'No Evaluado')], max_length=1)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.persona', verbose_name='Relacion del candidato con informacion de persona')),
                ('vacante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.vacante', verbose_name='Relacion de candidato con la vacante')),
            ],
        ),
    ]
