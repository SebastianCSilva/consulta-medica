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
    path('pacientes',views.paciente_list, name='paciente.html'),
    path('paciente/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('paciente/new', views.paciente_new, name='paciente_new'),
    path('paciente/<int:pk>/edit/', views.paciente_edit, name='paciente_edit'),

]