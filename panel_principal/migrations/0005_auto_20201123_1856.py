# Generated by Django 3.1.3 on 2020-11-23 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_principal', '0004_auto_20201119_0433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='llamada_medica',
            old_name='id_notificaciones',
            new_name='id_notification',
        ),
    ]
