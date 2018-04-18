
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('config/',views.config, name='config'),
    path('selectuser/',views.selectUser, name='selectuser'),
    path('adduser/',views.addUser, name='adduser'),
]
