from django.urls import path
from . import views

app_name = 'getObservations'
urlpatterns = [
    path('test/',views.test, name='test'),
    path('contodb/',views.contodb,name='contodb'),
]