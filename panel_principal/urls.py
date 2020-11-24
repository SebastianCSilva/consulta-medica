from django.urls import path
from . import views

urlpatterns = [
    path('', views.horas_list, name='horas_list'),
    #path('index', name='index.html'),
]