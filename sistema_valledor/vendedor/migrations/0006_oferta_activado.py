# Generated by Django 2.1.7 on 2019-04-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0005_auto_20190401_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='activado',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Oferta activada?'),
        ),
    ]