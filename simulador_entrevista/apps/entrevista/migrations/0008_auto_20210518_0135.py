# Generated by Django 3.2.3 on 2021-05-18 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrevista', '0007_auto_20210518_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrevista',
            name='fechaActualizacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 18, 1, 35, 19, 213118)),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 18, 1, 35, 19, 213118)),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fechaActualizacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 18, 1, 35, 19, 214119)),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 18, 1, 35, 19, 214119)),
        ),
    ]
