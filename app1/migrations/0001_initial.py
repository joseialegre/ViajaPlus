# Generated by Django 4.2.7 on 2023-11-30 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('nombre', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Itinerario',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('horario_partida', models.TimeField(blank=True, null=True)),
                ('horario_llegada', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'itinerario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pasaje',
            fields=[
                ('idpasaje', models.IntegerField(db_column='idPasaje', primary_key=True, serialize=False)),
                ('costo', models.IntegerField()),
            ],
            options={
                'db_table': 'pasaje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('numero_servicio', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_partida', models.DateField(blank=True, null=True)),
                ('fecha_llegada', models.DateField(blank=True, null=True)),
                ('calidad_servicio', models.CharField(blank=True, max_length=45, null=True)),
                ('disponibilidad', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('codigo', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('categoria', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('disponibilidad', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'transporte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('itinerario_codigo', models.OneToOneField(db_column='itinerario_codigo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.itinerario')),
                ('posicion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'parada',
                'managed': False,
            },
        ),
    ]