# Generated by Django 2.0.2 on 2018-12-26 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_auto_20181225_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='corte',
            name='ingreso',
            field=models.DecimalField(decimal_places=2, default=5.5, max_digits=15, verbose_name='Ingreso'),
            preserve_default=False,
        ),
    ]
