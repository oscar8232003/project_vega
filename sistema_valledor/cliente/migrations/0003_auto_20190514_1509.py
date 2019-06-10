# Generated by Django 2.1.7 on 2019-05-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20190401_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listas',
            name='comentarios',
        ),
        migrations.RemoveField(
            model_name='listas',
            name='estado',
        ),
        migrations.AddField(
            model_name='listas',
            name='comentario_cliente',
            field=models.TextField(blank=True, null=True, verbose_name='Comentario de cliente'),
        ),
        migrations.AddField(
            model_name='listas',
            name='comentario_vendedor',
            field=models.TextField(blank=True, null=True, verbose_name='Comentario de vendedor'),
        ),
        migrations.AddField(
            model_name='listas',
            name='estado_lista',
            field=models.CharField(blank=True, choices=[('normal', 'Normal'), ('enviada', 'Enviada'), ('cancelada', 'Cancelada'), ('armando_pedido', 'Armando Pedido'), ('lista_retiro', 'Listo para retirar'), ('completada', 'Lista completada'), ('no_retirada', 'No retirada')], max_length=200, null=True, verbose_name='Estado de la lista'),
        ),
    ]