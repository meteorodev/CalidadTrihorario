from django.db import models

# Create your models here.
class estacionpd(models.Model):
    estacion=models.CharField(max_length=5)
    municipio=models.CharField(max_length=4)
    nombreEstacion=models.CharField(max_length=200)
    latitud2=models.FloatField(default=None)
    longitud2 = models.FloatField(default=None)
    altitud = models.FloatField(default=None)

    def __init__(self,estacion,municipio,nombreEstacion,latitud2,longitud2,altitud):
        self.estacion = estacion
        self.municipio = municipio
        self.nombreEstacion = nombreEstacion
        self.latitud2 = latitud2
        self.longitud2 = longitud2
        self.altitud = altitud


