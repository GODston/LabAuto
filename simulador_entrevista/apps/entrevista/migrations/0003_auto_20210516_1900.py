# Generated by Django 3.2.3 on 2021-05-17 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrevista', '0002_auto_20210516_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrevista',
            name='fechaActualizacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 19, 0, 15, 141857)),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 19, 0, 15, 141857)),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fechaActualizacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 19, 0, 15, 141857)),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 19, 0, 15, 141857)),
        ),
    ]