from django.db import models
from django.utils import timezone


# Create your models here.
# AQUI TENEMOS QUE MODELAR LA BASE DE DATOS


"""
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""
class Generos(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

class Boxes(models.Model):
    numero = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.numero

class Pacientes(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    rut = models.TextField()
    fecha_nacimiento = models.TextField()
    direccion = models.TextField()
    """celular = models.TextField()
    correo = models.models.EmailField()"""
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.nombre_completo



class Medicos(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    rut = models.TextField()
    contrasena = models.TextField()
    direccion = models.TextField()
    fecha_nacimiento = models.TextField()
    """celular = models.TextField()
    correo = models.models.EmailField()"""
    
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nombre_completo


class Notificaciones(models.Model):
    """
    FALTA POR HACER LAS NOTIFICACIONES 
    """
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Horas_medicas(models.Model):
    id_boxes = models.ForeignKey(Boxes, on_delete=models.CASCADE)
    id_nombre_medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    id_nombre_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    fecha = models.DateTimeField(
            blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    
"""
    def __str__(self):
        return self.title
"""

class Llamada_medica(models.Model):
    id_notificaciones = models.ForeignKey(Notificaciones, on_delete=models.CASCADE)
    id_hora_medica = models.ForeignKey(Horas_medicas, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    """
    def __str__(self):
        return self.title
    """
