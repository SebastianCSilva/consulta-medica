# Generated by Django 3.1.3 on 2020-11-24 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_principal', '0006_auto_20201123_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas_medica',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]