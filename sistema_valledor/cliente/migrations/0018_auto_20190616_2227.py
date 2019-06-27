# Generated by Django 2.1.7 on 2019-06-17 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0013_productos_maximo_prod_comprar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0017_auto_20190606_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte_productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='ID Lista')),
                ('producto', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='ID Producto')),
                ('nombre_producto', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre Producto')),
                ('cantidad', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cantidad Comprada')),
                ('oferta', models.BooleanField(blank=True, default=False, null=True, verbose_name='Producto en Oferta')),
                ('Total', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Total')),
                ('fecha_registro', models.DateField(blank=True, null=True, verbose_name='Fecha de registro')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('local', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.Local')),
            ],
            options={
                'verbose_name': 'Reporte de Productos',
                'verbose_name_plural': 'Reporte de Productos',
            },
        ),
        migrations.AlterModelOptions(
            name='registro_listas',
            options={'verbose_name': 'Auditoria de Listas', 'verbose_name_plural': 'Auditoria de Listas'},
        ),
        migrations.AlterModelOptions(
            name='registro_premium',
            options={'verbose_name': 'Auditoria de premium', 'verbose_name_plural': 'Auditoria de premium'},
        ),
    ]
