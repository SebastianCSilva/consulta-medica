from django import forms

from .models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'direccion', 'genero')