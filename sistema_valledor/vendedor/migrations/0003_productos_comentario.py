# Generated by Django 2.1.7 on 2019-03-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0002_auto_20190330_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='comentario',
            field=models.TextField(blank=True, null=True, verbose_name='Comentarios'),
        ),
    ]