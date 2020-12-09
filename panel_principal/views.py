from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import PacienteForm, MedicoForm, HorasMedicasForm, LlamadasMedicasForm, NotificacionesForm
from .models import Boxe, Paciente, Medico, Notificacione, Horas_medica, Llamada_medica
from django.http import HttpResponse
import csv
from datetime import datetime
import pytz
from django.utils.dateparse import parse_datetime



# Create your views here.
def horas_list(request):
    llamadas = Llamada_medica.objects.filter().order_by('created_date')
    return render(request, 'panel_principal/templates/horas_list.html', {'llamadas': llamadas})


def pantalla_plana(request):
    return render(request, 'index.html',{})



def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def register(request):
    # Creamos el formulario de autenticación vacío
    
    form = UserCreationForm()

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                dj_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})

def login(request):
    error_message = None
    heading = 'Login Form'
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                dj_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


def paciente_list(request):
    pacientes = Paciente.objects.order_by('rut')
    return render(request, 'panel_principal/templates/paciente.html', {'pacientes':pacientes})

def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'paciente_detail.html', {'paciente': paciente})

def paciente_new(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.created_date = timezone.now()
            paciente.save()
            return redirect('paciente_detail', pk=paciente.pk)
    else:
        form = PacienteForm()
    return render(request, 'paciente_edit.html', {'form': form})

def paciente_edit(request, pk):
    post = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=post)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.created_date = timezone.now()
            paciente.save()
            return redirect('paciente_detail', pk=paciente.pk)
    else:
        form = PacienteForm(instance=post)
    return render(request, 'paciente_edit.html', {'form': form})



def medico_list(request):
    medicos = Medico.objects.order_by('rut')
    return render(request, 'medico.html', {'medicos':medicos})

def medico_detail(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    return render(request, 'medico_detail.html', {'medico': medico})

def medico_new(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            medico = form.save(commit=False)
            medico.created_date = timezone.now()
            medico.save()
            return redirect('medico_detail', pk=medico.pk)
    else:
        form = MedicoForm()
    return render(request, 'medico_edit.html', {'form': form})



def medico_edit(request, pk):
    post = get_object_or_404(Medico, pk=pk)
    if request.method == "POST":
        form = MedicoForm(request.POST, instance=post)
        if form.is_valid():
            medico = form.save(commit=False)
            medico.created_date = timezone.now()
            medico.save()
            return redirect('medico_detail', pk=medico.pk)
    else:
        form = MedicoForm(instance=post)
    return render(request, 'medico_edit.html', {'form': form})





def horasmedica_list(request):
    horasmedicas = Horas_medica.objects.order_by('id')
    return render(request, 'horasmedica.html', {'horasmedicas':horasmedicas})

def horasmedica_detail(request, pk):
    horasmedica = get_object_or_404(Horas_medica, pk=pk)
    return render(request, 'horasmedica_detail.html', {'horasmedica': horasmedica})

def horasmedica_new(request):
    if request.method == "POST":
        form = HorasMedicasForm(request.POST)
        if form.is_valid():
            horasmedica = form.save(commit=False)
            horasmedica.created_date = timezone.now()
            horasmedica.save()
            return redirect('horasmedica_detail', pk=horasmedica.pk)
    else:
        form = HorasMedicasForm()
    return render(request, 'horasmedica_edit.html', {'form': form})

def horasmedica_edit(request, pk):
    post = get_object_or_404(Horas_medica, pk=pk)
    if request.method == "POST":
        form = HorasMedicasForm(request.POST, instance=post)
        if form.is_valid():
            horasmedica = form.save(commit=False)
            horasmedica.created_date = timezone.now()
            horasmedica.save()
            return redirect('horasmedica_detail', pk=horasmedica.pk)
    else:
        form = HorasMedicasForm(instance=post)
    return render(request, 'horasmedica_edit.html', {'form': form})


def llamadasmedica_list(request):
    llamadasmedicas = Llamada_medica.objects.order_by('created_date')
    return render(request, 'panel_principal/templates/llamadasmedica.html', {'llamadasmedicas':llamadasmedicas})

def llamadasmedica_detail(request, pk):
    llamadasmedica = get_object_or_404(Llamada_medica, pk=pk)
    return render(request, 'llamadasmedica_detail.html', {'llamadasmedica': llamadasmedica})

def llamadasmedica_new(request):
    if request.method == "POST":
        form = LlamadasMedicasForm(request.POST)
        if form.is_valid():
            llamadasmedica = form.save(commit=False)
            llamadasmedica.created_date = timezone.now()
            llamadasmedica.save()
            return redirect('llamadasmedica_detail', pk=llamadasmedica.pk)
    else:
        form = LlamadasMedicasForm()
    return render(request, 'llamadasmedica_edit.html', {'form': form})

def llamadasmedica_edit(request, pk):
    post = get_object_or_404(Llamada_medica, pk=pk)
    if request.method == "POST":
        form = LlamadasMedicasForm(request.POST, instance=post)
        if form.is_valid():
            llamadasmedica = form.save(commit=False)
            llamadasmedica.created_date = timezone.now()
            llamadasmedica.save()
            return redirect('llamadasmedica_detail', pk=llamadasmedica.pk)
    else:
        form = LlamadasMedicasForm(instance=post)
    return render(request, 'llamadasmedica_edit.html', {'form': form})


def notificacione_list(request):
    notificaciones = Notificacione.objects.order_by('created_date')
    return render(request, 'panel_principal/templates/notificacione.html', {'notificaciones':notificaciones})

def notificacione_detail(request, pk):
    notificacione = get_object_or_404(Notificacione, pk=pk)
    return render(request, 'notificacione_detail.html', {'notificacione': notificacione})

def notificacione_new(request):
    if request.method == "POST":
        form = NotificacionesForm(request.POST)
        if form.is_valid():
            notificacione = form.save(commit=False)
            notificacione.created_date = timezone.now()
            notificacione.save()
            return redirect('notificacione_detail', pk=notificacione.pk)
    else:
        form = NotificacionesForm()
    return render(request, 'notificacione_edit.html', {'form': form})

def notificacione_edit(request, pk):
    post = get_object_or_404(Notificacione, pk=pk)
    if request.method == "POST":
        form = NotificacionesForm(request.POST, instance=post)
        if form.is_valid():
            notificacione = form.save(commit=False)
            notificacione.created_date = timezone.now()
            notificacione.save()
            return redirect('notificacione_detail', pk=notificacione.pk)
    else:
        form = NotificacionesForm(instance=post)
    return render(request, 'notificacione_edit.html', {'form': form})


def export_csv(request, fechainicio, fechafinal):
    response = HttpResponse(content_type='text/csv')
   
    fechainicio1 = fechainicio
    fechafinal1 = fechafinal
     
    print(str(fechainicio1)+' 00:00:00.000000' +'/// '+ str(fechafinal1)+' 00:00:00.000000')
    fechaauxiliar = str(fechainicio1)+' 00:00:00.000000'
    fechaauxiliar2 = str(fechafinal1)+' 00:00:00.000000'
  
    

    fechainicioformateada = datetime.strptime(fechaauxiliar, "%Y-%m-%d %H:%M:%S.%f")
    fechafinalformateada = datetime.strptime(fechaauxiliar2, "%Y-%m-%d %H:%M:%S.%f")
   
    

    la = pytz.timezone('America/Santiago')
    
    n1 = parse_datetime(fechaauxiliar) # naive object
    n2 = parse_datetime(fechaauxiliar2)
    aware_start_time = la.localize(n1) # aware object
    aware_end_time = la.localize(n2)
    print(aware_start_time)
    print(aware_end_time)

    writer = csv.writer(response)
    writer.writerow(['Nombre del Doctor','Box','Fecha Creado'])

    for horasmedicas in Horas_medica.objects.order_by('id_medico').values_list('id_medico','id_boxes','id_paciente','created_date'):
        
        formarcsv = ''
        formafinal = []
        if (horasmedicas[3] <= aware_end_time and horasmedicas[3] >= aware_start_time):
            #Esto esta funcionando para hacer comparacion de las fechas y solo filtrar las que necesitamos
            
            #ID MEDICO
            if horasmedicas[0] != None:
                idmedico = horasmedicas[0]
                nombredoctor = Medico.objects.filter(pk=idmedico).values_list('nombre','apellidos')
                print(nombredoctor)
                
                formarcsv = ' '.join(str(x) for x in nombredoctor)
                print(formarcsv)
            print(nombredoctor[0])
            print(nombredoctor[0])
            print(nombredoctor[0])
            print(nombredoctor[0])
            """#ID PACIENTE
            if horasmedicas[2] != None:
                formarcsv = formarcsv + horasmedicas[2]
                print(horasmedicas[2])"""

            if horasmedicas[3] != None:
                #formarcsv = formarcsv +","+ str(horasmedicas[3].date())
                print(horasmedicas[3])
            print(formarcsv)
            formafinal = [formarcsv,horasmedicas[1],horasmedicas[3].date()]
            writer.writerow(formafinal)

    response['Content-Disposition'] = 'attachment; filename="medicos.csv"'
    
    return response