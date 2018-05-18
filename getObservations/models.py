from django.db import models

# Create your models here.
# Create your models here.
class Estacion(models.Model):
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
    def cargaEstaciones(self):
        pass


####Modelo para datos mensuales
# _*_ coding: utf-8 *_*
#Autor: Darwin Rosero Vaca
#Descripción: clase modelo para datos mensuales

class MesData():
    """representa la tabla de datos mensuales de la base mch"""
    codigo=models.CharField(max_length=5)
    año=models.IntegerField(max_length=4)
    ene = models.FloatField(max_length=8)
    feb = models.FloatField(max_length=8)
    mar = models.FloatField(max_length=8)
    abr = models.FloatField(max_length=8)
    may = models.FloatField(max_length=8)
    jun = models.FloatField(max_length=8)
    jul = models.FloatField(max_length=8)
    ago = models.FloatField(max_length=8)
    sep = models.FloatField(max_length=8)
    oct = models.FloatField(max_length=8)
    nov = models.FloatField(max_length=8)
    dic = models.FloatField(max_length=8)

    def __init__(self,):
        """Constructor for """

