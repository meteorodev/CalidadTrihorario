from django.shortcuts import render
from django.http import Http404, HttpResponse
from base_consulta.models import BaseConf
from .models import estacionpd
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


## vista de coinexion a la base de datos
def contodb(request):
    # try:
    mchcred = dbConf("darosero")
    print(mchcred.db_user + " ######## log")
    conne = mch.MchConect(mchcred.db_host, mchcred.db_user, mchcred.db_pass, mchcred.db_name)
    data = conne.consulta("select estacion, municipio, nombreEstacion, latitud2" +
                          ",longitud2,altitud from estaciones where estacion like 'M%' order by estacion;")
    print(type(mchcred))
    dataE = []  # Lista de estaciones
    for d in data:
        epd = estacionpd(d[0], d[1], d[2], d[3], d[4], d[5])
        dataE.append(epd)
    #print(len(dataE))
    # except:
    #    raise Http404("Error al conectar a la base")
    return render(request, 'getObservations/contodb.html', {'milista': mchcred, 'estaciones': dataE})

