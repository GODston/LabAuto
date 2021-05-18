# Generated by Django 3.2 on 2021-05-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ap_paterno', models.CharField(max_length=30)),
                ('ap_materno', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('correo', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=14)),
            ],
        ),
    ]
