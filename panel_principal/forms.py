from django import forms

from .models import Paciente, Medico

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'direccion', 'genero')

class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = ('nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'direccion', 'genero')
