# Generated by Django 4.2.7 on 2023-12-01 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='itinerario',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='pasaje',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='transporte',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='ciudad',
            table='ciudad',
        ),
        migrations.AlterModelTable(
            name='itinerario',
            table='itinerario',
        ),
        migrations.AlterModelTable(
            name='pasaje',
            table='pasaje',
        ),
        migrations.AlterModelTable(
            name='servicio',
            table='servicio',
        ),
        migrations.AlterModelTable(
            name='transporte',
            table='transporte',
        ),
        migrations.DeleteModel(
            name='Parada',
        ),
    ]
