# Generated by Django 3.2.3 on 2021-05-18 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_alter_empresa_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='nombre',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='vacante',
            old_name='nombre',
            new_name='vacante',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='password',
        ),
    ]
