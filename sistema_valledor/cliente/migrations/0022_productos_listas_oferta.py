# Generated by Django 2.1.7 on 2019-06-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0021_auto_20190621_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos_listas',
            name='oferta',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Producto en Oferta'),
        ),
    ]