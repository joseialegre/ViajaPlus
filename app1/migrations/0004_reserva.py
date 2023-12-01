# Generated by Django 4.2.7 on 2023-12-01 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_servicio_calidad_servicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('codigo', models.IntegerField(db_column='codigo', primary_key=True, serialize=False)),
                ('dni', models.IntegerField(blank=True, db_column='DNI', null=True)),
                ('idPasaje', models.ForeignKey(db_column='idPasaje', on_delete=django.db.models.deletion.DO_NOTHING, to='app1.pasaje')),
            ],
            options={
                'db_table': 'reserva',
                'managed': True,
            },
        ),
    ]