from django.urls import path
from . import views

app_name = 'getObservations'
urlpatterns = [
    path('test/',views.test, name='test'),
    path('estaciones/',views.estaciones,name='estaciones'),
    path('estacionesp/',views.estacionesPag,name='estacionesp'),
    path('detalleEst/?P<estacion>',views.detalleEst,name='detalleEst'),
    path('detalleEst/',views.detalleEst,name='detalleEst'),
]