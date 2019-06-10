# Generated by Django 2.1.7 on 2019-05-14 18:33

from django.db import migrations, models
import vendedor.models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0011_auto_20190505_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='imagen_banner',
            field=models.ImageField(blank=True, default='vendedor/Mi_Tienda.png', null=True, upload_to=vendedor.models.borrar_imagen_anterior_local_banner, verbose_name='Imagen de Banner'),
        ),
        migrations.AlterField(
            model_name='local',
            name='imagen_muestra',
            field=models.ImageField(blank=True, default='core/sin_imagen.jpg', null=True, upload_to=vendedor.models.borrar_imagen_anterior_local_muestra, verbose_name='Imagen de muestra'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, default='core/sin_imagen.jpg', null=True, upload_to=vendedor.models.borrar_imagen_anterior_producto),
        ),
    ]
