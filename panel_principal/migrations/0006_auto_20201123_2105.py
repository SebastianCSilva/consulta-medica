# Generated by Django 3.1.3 on 2020-11-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_principal', '0005_auto_20201123_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas_medica',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
