# Generated by Django 2.1.7 on 2019-06-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20190327_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_usuarios',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio del Premium'),
        ),
    ]
