from django.shortcuts import render
from django.http import HttpResponse
from util.loadConfig import LoadConfig



# Create your views here.
def index(request):
    lc=LoadConfig()
    lc.getConfig()
    return HttpResponse("Soy la funcion index.")

def config(request):
    return HttpResponse("Soy la funcion config")

def selectUser(request):
    return HttpResponse("Soy la funcion select user")

def addUser(request):
    return HttpResponse("soy la funcion add User")