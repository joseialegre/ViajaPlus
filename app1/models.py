from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(primary_key=True, max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'ciudad'


class Itinerario(models.Model):
    codigo = models.IntegerField(primary_key=True)
    horario_partida = models.TimeField(blank=True, null=True)
    horario_llegada = models.TimeField(blank=True, null=True)
    origen = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='origen')
    destino = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='destino', related_name='itinerario_destino_set')

    def __str__(self):
        return str(self.codigo)

    class Meta:
        managed = False
        db_table = 'itinerario'


class Parada(models.Model):
    itinerario = models.ForeignKey(Itinerario, models.DO_NOTHING, db_column='itinerario_codigo')
    ciudad_nombre = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_nombre')
    posicion = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.ciudad_nombre)

    class Meta:
        managed = False
        db_table = 'parada'
        unique_together = (('itinerario', 'ciudad_nombre'),)


class Pasaje(models.Model):
    idpasaje = models.IntegerField(db_column='idPasaje', primary_key=True)  # Field name made lowercase.
    costo = models.IntegerField()
    servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio')

    def __str__(self):
        return str(self.idpasaje)

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

    def __str__(self):
        return str(self.numero_servicio)

    class Meta:
        managed = False
        db_table = 'servicio'


class Transporte(models.Model):
    codigo = models.CharField(primary_key=True, max_length=45)
    categoria = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    disponibilidad = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.codigo)

    class Meta:
        managed = False
        db_table = 'transporte'

