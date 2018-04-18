from django.shortcuts import render
from django.http import HttpResponse
from util.loadConfig import LoadConfig
from .models import BaseConf


# Create your views here.
def index(request):
    ##lc=LoadConfig()
    #lc.getConfig()
    listHost=BaseConf.objects.all()
    out=[]
    for b in listHost:
        out.append(b.db_host+" : "+b.db_desc)
    return HttpResponse(out)

def config(request):
    return HttpResponse("Soy la funcion config")

def selectUser(request):
    return HttpResponse("Soy la funcion select user")

def addUser(request):
    return HttpResponse("soy la funcion add User")