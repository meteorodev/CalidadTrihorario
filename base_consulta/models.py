# _*_ coding: utf-8 *_*
#Autor: Darwin Rosero Vaca
#Descripción: CLASES MODELO, CONFIGURACIÓN DE LA BASE DE DATOS DE CONSULTA
from django.db import models

# Create your models here.
class BaseConf(models.Model):
    db_host = models.CharField(max_length=15)
    db_user = models.CharField(max_length=60)
    db_pass = models.CharField(max_length=60)
    db_name = models.CharField(max_length=60)
    db_desc = models.CharField(max_length=200)
    db_esta =models.IntegerField()

    def __str__(self):
        return print(self.db_host," ",self.db_user," ",self.db_desc)


class Variables():
    """vARIABLES DE CONSULTA DE LA BASE DE DATOS EN CASO DE QUE
     SE REALICE LA CONSULTA A VARIAS TABLAS"""
    nombre_var= models.CharField(max_length=100)
    uni_med = models.CharField(max_length=100)
    def __init__(self,):

        """Constructor for Variables"""
