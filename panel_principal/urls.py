from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.horas_list, name='horas_list'),
    path('index',views.pantalla_plana, name='index.html'),
    path('welcome', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]