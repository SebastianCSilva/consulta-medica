from django import forms

from .models import Paciente, Medico, Horas_medica, Llamada_medica, Notificacione

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

class LlamadasMedicasForm(forms.ModelForm):

    class Meta:
        model = Llamada_medica
        fields = ('id_hora_medica', 'id_notification', 'llamadas')

class NotificacionesForm(forms.ModelForm):

    class Meta:
        model = Notificacione
        fields = ('nombrecompleto', 'rut')