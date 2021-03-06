# Generated by Django 2.0.2 on 2019-02-10 01:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0009_auto_20190127_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excepcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('Matutino', 'Matutino'), ('Nocturno', 'Nocturno'), ('Completo', 'Completo')], max_length=50, verbose_name='Turno')),
                ('folio', models.PositiveSmallIntegerField(verbose_name='Folio')),
                ('activo', models.BooleanField(verbose_name='Activo')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de pago')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultimo Pago')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Costo')),
                ('sucursal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_excepcion', to='admin_app.Sucursal', verbose_name='Sucursal')),
            ],
            options={
                'verbose_name': 'Excepcion',
                'verbose_name_plural': 'Excepciones',
                'ordering': ['-folio'],
            },
        ),
    ]
