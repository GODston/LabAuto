# Generated by Django 3.1.2 on 2021-05-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterio',
            name='puntuacion',
            field=models.IntegerField(default=0),
        ),
    ]
