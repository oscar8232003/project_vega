# Generated by Django 2.1.7 on 2019-04-01 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendedor', '0003_productos_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre del Local')),
                ('total', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Total de la lista')),
                ('fecha_enviado', models.DateField(blank=True, null=True, verbose_name='Fecha de envio de la lista')),
                ('fecha_expiracion', models.DateField(blank=True, null=True, verbose_name='Fecha de expiracion de la lista')),
                ('comentarios', models.TextField(blank=True, null=True, verbose_name='Comentarios')),
                ('estado', models.BooleanField(blank=True, default='normal', null=True, verbose_name='Estado de la lista')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedor.Local')),
            ],
            options={
                'verbose_name': 'Listas',
                'verbose_name_plural': 'Listas',
            },
        ),
        migrations.CreateModel(
            name='Productos_listas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cantidad a comprar')),
                ('comentarios', models.TextField(blank=True, null=True, verbose_name='Comentarios del productos a comprar')),
                ('precio_producto', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Precio actual del producto a comprar')),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Listas')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedor.Local')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedor.Productos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Producto de la lista',
                'verbose_name_plural': 'Productos de las listas',
            },
        ),
    ]