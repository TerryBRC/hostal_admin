# Generated by Django 5.0.6 on 2024-06-04 07:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservas', '0002_alter_reserva_fecha_creacion_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Cobro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cobro', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Tipo de Cobro',
                'verbose_name_plural': 'Tipos de Cobros',
                'db_table': 'tipo_cobro',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de Emisión')),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('detalle_servicios', models.TextField()),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.reserva')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Facturador')),
                ('tipo_cobro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.tipo_cobro', verbose_name='Tipo de Cobro')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'db_table': 'factura',
            },
        ),
    ]