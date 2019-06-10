# Generated by Django 2.1.7 on 2019-06-02 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0013_productos_maximo_prod_comprar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0012_auto_20190602_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_de_productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Accion realizada')),
                ('fecha_registro', models.DateField(blank=True, null=True, verbose_name='Fecha de registro')),
                ('valores_antiguos', models.TextField(blank=True, null=True, verbose_name='Valores a Cambiar')),
                ('valores_nuevos', models.TextField(blank=True, null=True, verbose_name='Vaoles nuevos')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.Productos')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Registro de Productos',
            },
        ),
        migrations.RemoveField(
            model_name='registro_premium',
            name='tipo_usuario',
        ),
        migrations.AddField(
            model_name='registro_listas',
            name='cantidad_productos',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Total de productos'),
        ),
        migrations.DeleteModel(
            name='Registro_premium',
        ),
    ]
