# Generated by Django 2.1.7 on 2019-06-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0013_auto_20190602_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='listas',
            name='total_marcado',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Total de los productos marcados'),
        ),
    ]
