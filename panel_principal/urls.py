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
    #
    path('pacientes',views.paciente_list, name='paciente.html'),
    path('paciente/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('paciente/new', views.paciente_new, name='paciente_new'),
    path('paciente/<int:pk>/edit/', views.paciente_edit, name='paciente_edit'),
    #
    path('medicos',views.medico_list, name='medico.html'),
    path('medico/<int:pk>/', views.medico_detail, name='medico_detail'),
    path('medico/new', views.medico_new, name='medico_new'),
    path('medico/<int:pk>/edit/', views.medico_edit, name='medico_edit'),
    #
    path('horasmedicas',views.horasmedica_list, name='horasmedica.html'),
    path('horasmedica/<int:pk>/', views.horasmedica_detail, name='horasmedica_detail'),
    path('horasmedica/new', views.horasmedica_new, name='horasmedica_new'),
    path('horasmedica/<int:pk>/edit/', views.horasmedica_edit, name='horasmedica_edit'),
    #
    path('llamadasmedicas',views.llamadasmedica_list, name='llamadasmedica.html'),
    path('llamadasmedica/<int:pk>/', views.llamadasmedica_detail, name='llamadasmedica_detail'),
    path('llamadasmedica/new', views.llamadasmedica_new, name='llamadasmedica_new'),
    path('llamadasmedica/<int:pk>/edit/', views.llamadasmedica_edit, name='llamadasmedica_edit'),
    #
    path('notificaciones',views.notificacione_list, name='notificacione.html'),
    path('notificacione/<int:pk>/', views.notificacione_detail, name='notificacione_detail'),
    path('notificacione/new', views.notificacione_new, name='notificacione_new'),
    path('notificacione/<int:pk>/edit/', views.notificacione_edit, name='notificacione_edit'),
    #, name='export_csv'  ?P<fechainicio>\w/?P<fechafinal>\w/
    path('exportcsv/<str:fechainicio>/<str:fechafinal>/', views.export_csv),
]