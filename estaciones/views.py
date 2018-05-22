from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import random

from base_consulta.models import BaseConf
from getObservations.models import Estacion
from .models import Estacion
import util.loadConfig as lc
import util.mchConect as mch


## this function just call load config and mch conn
def dbConf(user):
    """write this function for to conect sqlte3 and get users credentials for the databses"""
    ##dbconf=lc.LoadConfig()
    ##dbconf.getConfig("darosero")
    listHost = BaseConf.objects.get(db_user=user)
    return listHost


# Create your views here.

def listaest(request):
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
        paginator = Paginator(dataE, 10)
        page = request.GET.get('page')
        lisEst = paginator.get_page(page)

    except:
        raise Http404("Error de conexión")
    return render(request, 'estaciones/listaest.html', {'estaciones': lisEst})


def detest(request, estacion):
    print("view detest ", estacion)
    try:
        mchcred = dbConf("darosero")
        # print(mchcred.db_user + " ######## log")
        conne = mch.MchConect(mchcred.db_host, mchcred.db_user, mchcred.db_pass, mchcred.db_name)
        data = conne.consulta("select estacion, municipio, nombreEstacion, latitud2" +
                              ",longitud2,altitud from estaciones where estacion='" + estacion + "' order by estacion;")
        dataE = data[0]
        print(dataE)

        # print("antes de crear el objeto ",dataE[0],dataE[1],dataE[2],dataE[3],dataE[4],dataE[5])
        est = Estacion(dataE[0],dataE[1],dataE[2],dataE[3],dataE[4],dataE[5])
        print(est)
    except:
        raise Http404("Error de conexión")
    return render(request, 'estaciones/detest.html', {'est': est})
