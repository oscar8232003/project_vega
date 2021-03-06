# Generated by Django 2.1.7 on 2019-03-25 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.CharField(blank=True, default='cliente', max_length=200, null=True, verbose_name='Tipo de Usuario')),
                ('tipo_premium', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Tipo de Premium')),
                ('fecha_caducidad', models.DateField(blank=True, null=True, verbose_name='Fecha de Caducidad del Premium')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo de Usuarios',
                'verbose_name_plural': 'Tipos de Usuarios',
                'ordering': ['tipo_usuario', 'fecha_caducidad', 'id'],
            },
        ),
    ]
