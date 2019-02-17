# Generated by Django 2.0.2 on 2019-02-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suscripcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscripcion',
            name='tipo',
            field=models.CharField(choices=[('Locatario', 'Locatario'), ('Pensionado', 'Pensionado'), ('Otro', 'Otro')], default='Locatario', max_length=50, verbose_name='tipo'),
        ),
    ]