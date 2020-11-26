from django import forms

from .models import Paciente, Medico, Horas_medica

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'direccion', 'genero')

class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = ('nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'direccion', 'genero')

class HorasMedicasForm(forms.ModelForm):

    class Meta:
        model = Horas_medica
        fields = ('id_boxes', 'id_medico', 'id_paciente', 'descripcion', 'diagnostico')