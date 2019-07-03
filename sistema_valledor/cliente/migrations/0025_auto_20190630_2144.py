# Generated by Django 2.1.7 on 2019-07-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0024_auto_20190630_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listas',
            name='estado_lista',
            field=models.CharField(blank=True, choices=[('lista_retiro', 'Listo para retirar'), ('armando_pedido', 'Armando Pedido'), ('normal', 'Normal'), ('enviada', 'Enviada'), ('cancelada', 'Cancelada'), ('no_retirada', 'No retirada'), ('completada', 'Lista completada')], default='normal', max_length=20, null=True, verbose_name='Estado de la lista'),
        ),
    ]