# Generated by Django 2.0.2 on 2019-02-10 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_app', '0011_excepcion_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='supervisor',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Supervisor'),
        ),
    ]
