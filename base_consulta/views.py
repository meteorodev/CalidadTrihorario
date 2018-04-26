from django.shortcuts import render
from django.http import Http404,HttpResponse
from django import forms
from django.shortcuts import render
from util.loadConfig import LoadConfig
from .models import BaseConf



# Create your views here.
def index(request):
    ##lc=LoadConfig()
    #lc.getConfig()
    try:
        listHost=BaseConf.objects.all()
        out=[]
        for b in listHost:
            out.append([b.db_host+" : "+b.db_desc])
    except:
        raise Http404("no hay host en la base")
    return render(request,'base_consulta/index.html',{'milista':listHost})

def config(request):

    class NameForm(forms.Form):
        f1=forms.CharField(label="Nombre",max_length=10)

    try:
        listHost = BaseConf.objects.all()
    except:
        raise Http404("no hay host en la base")
    return render(request,'base_consulta/config.html',{"form":NameForm,'milista':listHost})

def selectUser(request):
    return HttpResponse("Soy la funcion select user")

def addUser(request):
    return HttpResponse("soy la funcion add User")