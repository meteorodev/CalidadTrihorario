from django.urls import path
from . import views

app_name = 'estaciones'
urlpatterns = [
    path('listaest/',views.listaest,name='listaest'),
    path('detest/?P<estacion>',views.detest,name='detest'),
]