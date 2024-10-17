# Generated by Django 3.2.3 on 2023-05-14 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membresias', '0002_alter_cliente_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField()),
                ('precio_pago', models.FloatField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membresias.cliente')),
            ],
        ),
    ]
