from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import PacienteForm, MedicoForm
from .models import Boxe, Paciente, Medico, Notificacione, Horas_medica, Llamada_medica





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
                return redirect('/welcome')

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
            paciente.nombre = request.nombre
            paciente.apellidos = request.apellidos
            paciente.rut = request.rut
            paciente.nombre = request.nombre
            paciente.fecha_nacimiento = request.fecha_nacimiento
            paciente.direccion = request.direccion
            paciente.genero = request.genero
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
            paciente.nombre = request.nombre
            paciente.apellidos = request.apellidos
            paciente.rut = request.rut
            paciente.nombre = request.nombre
            paciente.fecha_nacimiento = request.fecha_nacimiento
            paciente.direccion = request.direccion
            paciente.genero = request.genero
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
            medico.nombre = request.nombre
            medico.apellidos = request.apellidos
            medico.rut = request.rut
            medico.fecha_nacimiento = request.fecha_nacimiento
            medico.direccion = request.direccion
            medico.genero = request.genero
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
            medico.nombre = request.nombre
            medico.apellidos = request.apellidos
            medico.rut = request.rut
            medico.fecha_nacimiento = request.fecha_nacimiento
            medico.direccion = request.direccion
            medico.genero = request.genero
            medico.created_date = timezone.now()
            medico.save()
            return redirect('medico_detail', pk=medico.pk)
    else:
        form = MedicoForm(instance=post)
    return render(request, 'medico_edit.html', {'form': form})