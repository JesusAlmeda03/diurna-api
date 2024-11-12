from django.db import models

# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=200, null=True)
    fecha = models.DateField(auto_now_add=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Participantes(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    escuela = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono =  models.CharField(max_length=15)



class Tutores(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    par = models.ForeignKey(Participantes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100) 
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)



class Estudiantes(models.Model):
    institucion = models.ForeignKey(Participantes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100, default='')
    materno= models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
