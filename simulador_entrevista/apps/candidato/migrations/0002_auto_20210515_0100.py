# Generated by Django 3.2 on 2021-05-15 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='fechaEntrevista',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidato',
            name='fechaRegistro',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
