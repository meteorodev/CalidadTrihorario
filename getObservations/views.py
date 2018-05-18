from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import random

from base_consulta.models import BaseConf
from getObservations.models import Estacion
from .models import Estacion,MesData
import util.loadConfig as lc
import util.mchConect as mch


# Create your views here.
## this function just call load config and mch conn
def dbConf(user):
    """write this function for to conect sqlte3 and get users credentials for the databses"""
    ##dbconf=lc.LoadConfig()
    ##dbconf.getConfig("darosero")
    listHost = BaseConf.objects.get(db_user=user)
    return listHost


## vista de test

def test(request):
    try:
        mchcred = BaseConf.objects.all()
        print(mchcred)
    except:
        raise Http404("no hay host en la base")
    return render(request, 'getObservations/test.html', {'milista': mchcred})


""" Modelos
db_host = models.CharField(max_length=15)
db_user = models.CharField(max_length=60)
db_pass = models.CharField(max_length=60)
db_name = models.CharField(max_length=60)
db_desc = models.CharField(max_length=200)
db_esta =models.IntegerField()
"""
## vista de conexion a la base de datos
def estaciones(request):
    try:
        mchcred = dbConf("darosero")
        print(mchcred.db_user + " ######## log")
        conne = mch.MchConect(mchcred.db_host, mchcred.db_user, mchcred.db_pass, mchcred.db_name)
        data = conne.consulta("select estacion, municipio, nombreEstacion, latitud2" +
                              ",longitud2,altitud from estaciones where estacion like 'M%' order by estacion;")
        dataE = []  # Lista de estaciones
        for d in data:
            epd = Estacion(d[0], d[1], d[2], d[3], d[4], d[5])
            dataE.append(epd)
        print(len(dataE))
    except:
        raise Http404("Error al conectar a la base")
    return render(request, 'getObservations/estaciones.html', {'milista': mchcred, 'estaciones': dataE})

def estacionesPag(request):
    try:

        mchcred = dbConf("darosero")
        print(mchcred.db_user + " ######## log")
        conne = mch.MchConect(mchcred.db_host, mchcred.db_user, mchcred.db_pass, mchcred.db_name)
        data = conne.consulta("select estacion, municipio, nombreEstacion, latitud2" +
                              ",longitud2,altitud from estaciones where estacion like 'M%' order by estacion;")
        dataE = []  # Lista de estaciones
        for d in data:
            epd = Estacion(d[0], d[1], d[2], d[3], d[4], d[5])
            dataE.append(epd)
        print(len(dataE))
        paginator=Paginator(dataE,10)
        page=request.GET.get('page')
        lisEst=paginator.get_page(page)

    except:
        raise Http404("Error de conexión")
    return render(request, 'getObservations/estacionesp.html', {'estaciones': lisEst })

def detalleEst(request,estacion):
    print(estacion)
    """try:
        dataE = []  # Lista de estaciones
        for d in range(0,20):
            epd = Estacion("Ficticia", "no existe", "nombre",random.randrange(d), random.randrange(d), random.randrange(d))
            dataE.append(epd)
        print(len(dataE))
        paginator=Paginator(dataE,10)
        page=request.GET.get('page')
        lisEst=paginator.get_page(page)

    except:
        raise Http404("Error de conexión")
        """
    return render(request, 'getObservations/detalleEst.html', {'estaciones': [estacion] })


def getmes(request,estacion='M0001',añoi=1981,añof=2010):
    try:
        mchcred = dbConf("darosero")
        print(mchcred.db_user + " ######## log")
        conne = mch.MchConect(mchcred.db_host, mchcred.db_user, mchcred.db_pass, mchcred.db_name)
        data = conne.consulta("select * from v0001 where codigo='"+estacion+"' and anio >= "+añoi+" and anio <= "+añof+" order by anio;")
        dataMes = []  # Lista de estaciones
        for d in data:
            mespd = MesData(codigo=d[0], año=d[1], ene=d[2], feb=d[3], mar=d[4], abr=d[5], may=d[6], jun=d[6],
                            jul=d[8], ago=d[9],sep=d[10], oct=d[11], nov=d[12], dic=d[13])
            dataMes.append(mespd)
        print(len(dataMes))
        paginator=Paginator(dataMes,10)
        page=request.GET.get('page')
        lisEst=paginator.get_page(page)

    except:
        raise Http404("Error de conexión")
    return render(request, 'getObservations/mesdata.html',{'mes':[1,2,3]})