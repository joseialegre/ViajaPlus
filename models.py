# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Itinerario(models.Model):
    codigo = models.IntegerField(primary_key=True)
    horario_partida = models.TimeField(blank=True, null=True)
    horario_llegada = models.TimeField(blank=True, null=True)
    origen = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='origen')
    destino = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='destino', related_name='itinerario_destino_set')

    class Meta:
        managed = False
        db_table = 'itinerario'


class Parada(models.Model):
    itinerario_codigo = models.OneToOneField(Itinerario, models.DO_NOTHING, db_column='itinerario_codigo', primary_key=True)  # The composite primary key (itinerario_codigo, ciudad_nombre) found, that is not supported. The first column is selected.
    ciudad_nombre = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_nombre')
    posicion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parada'
        unique_together = (('itinerario_codigo', 'ciudad_nombre'),)


class Pasaje(models.Model):
    idpasaje = models.IntegerField(db_column='idPasaje', primary_key=True)  # Field name made lowercase.
    costo = models.IntegerField()
    servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio')

    class Meta:
        managed = False
        db_table = 'pasaje'


class Servicio(models.Model):
    numero_servicio = models.IntegerField(primary_key=True)
    fecha_partida = models.DateField(blank=True, null=True)
    fecha_llegada = models.DateField(blank=True, null=True)
    calidad_servicio = models.CharField(max_length=45, blank=True, null=True)
    disponibilidad = models.CharField(max_length=45, blank=True, null=True)
    transporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='transporte')
    itinerario = models.ForeignKey(Itinerario, models.DO_NOTHING, db_column='itinerario')

    class Meta:
        managed = False
        db_table = 'servicio'


class Transporte(models.Model):
    codigo = models.CharField(primary_key=True, max_length=45)
    categoria = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    disponibilidad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transporte'
