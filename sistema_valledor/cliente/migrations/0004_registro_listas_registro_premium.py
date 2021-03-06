# Generated by Django 2.1.7 on 2019-05-15 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0012_auto_20190514_1433'),
        ('registration', '0003_auto_20190327_2348'),
        ('cliente', '0003_auto_20190514_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_listas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_lista', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre de la lista')),
                ('rut_cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rut')),
                ('fecha_registro', models.DateField(blank=True, null=True, verbose_name='Fecha de registro')),
                ('total', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total del pedido')),
                ('estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado del pedido')),
                ('lista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Listas')),
                ('local', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.Local')),
            ],
            options={
                'verbose_name': 'Auditoria de Listas',
            },
        ),
        migrations.CreateModel(
            name='Registro_premium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rut')),
                ('premium', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipo_premium')),
                ('fecha_comienzo', models.DateField(blank=True, null=True, verbose_name='Fecha de comienzo')),
                ('fecha_termino', models.DateField(blank=True, null=True, verbose_name='Fecha de termino')),
                ('pago', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total a pagar')),
                ('tipo_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Tipo_usuarios')),
            ],
            options={
                'verbose_name': 'Auditoria de Premium',
            },
        ),
    ]
