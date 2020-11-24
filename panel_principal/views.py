from django.shortcuts import render
from django.utils import timezone
from .models import Boxe, Paciente, Medico, Notificacione, Horas_medica, Llamada_medica


# Create your views here.
def horas_list(request):
    llamadas = Llamada_medica.objects.filter().order_by('created_date')
    return render(request, 'panel_principal/templates/horas_list.html', {'llamadas': llamadas})

"""
def pantalla_plana(request):
    return render(request, 'index.html',{})

"""