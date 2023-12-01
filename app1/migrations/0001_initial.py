# Generated by Django 4.2.7 on 2023-12-01 03:35

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
        ),
        migrations.CreateModel(
            name='Itinerario',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('codigo', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('categoria', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('disponibilidad', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('numero_servicio', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_partida', models.DateField(blank=True, null=True)),
                ('fecha_llegada', models.DateField(blank=True, null=True)),
                ('calidad_servicio', models.CharField(blank=True, max_length=45, null=True)),
                ('disponibilidad', models.CharField(blank=True, max_length=45, null=True)),
                ('itinerario', models.ForeignKey(db_column='itinerario', on_delete=django.db.models.deletion.DO_NOTHING, to='app1.itinerario')),
                ('transporte', models.ForeignKey(db_column='transporte', on_delete=django.db.models.deletion.DO_NOTHING, to='app1.transporte')),
            ],
        ),
        migrations.CreateModel(
            name='Pasaje',
            fields=[
                ('idpasaje', models.IntegerField(db_column='idPasaje', primary_key=True, serialize=False)),
                ('costo', models.IntegerField()),
                ('servicio', models.ForeignKey(db_column='servicio', on_delete=django.db.models.deletion.DO_NOTHING, to='app1.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('ciudad_nombre', models.ForeignKey(db_column='ciudad_nombre', on_delete=django.db.models.deletion.DO_NOTHING, to='app1.ciudad')),
                ('itinerario', models.ForeignKey(db_column='itinerario_codigo', on_delete=django.db.models.deletion.DO_NOTHING, to='app1.itinerario')),
            ],
            options={
                'unique_together': {('itinerario', 'ciudad_nombre')},
            },
        ),
    ]
