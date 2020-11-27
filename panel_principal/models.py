from django.db import models
from django.utils import timezone


# Create your models here.
# AQUI TENEMOS QUE MODELAR LA BASE DE DATOS

class Genero(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre


class Boxe(models.Model):
    numero = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.numero


class Paciente(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    rut = models.TextField()
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.rut, self.nombre, self.apellidos)


class Medico(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    rut = models.TextField()
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.rut, self.nombre, self.apellidos)


class Notificacione(models.Model):
    nombrecompleto = models.TextField(default='Nombre Completo')
    rut = models.TextField(default='91.111.111-1')
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.id, self.rut, self.nombrecompleto)


class Horas_medica(models.Model):
    id = models.AutoField(primary_key=True)
    id_boxes = models.ForeignKey(Boxe, on_delete=models.CASCADE)
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    diagnostico = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        #template = '{0.descripcion} {0.diagnostico}'
        return "%s %s %s" % (self.id, self.id_paciente.nombre, self.id_paciente.apellidos)


class Llamada_medica(models.Model):
    id_hora_medica = models.ForeignKey(Horas_medica, on_delete=models.CASCADE)
    id_notification = models.ForeignKey(
        Notificacione, on_delete=models.CASCADE)
    llamadas = models.PositiveIntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.id_hora_medica.id_paciente.nombre, self.id_hora_medica.id_paciente.apellidos, self.id_notification)
