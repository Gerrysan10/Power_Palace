# Generated by Django 3.2.3 on 2023-05-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membresias', '0003_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pago',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
