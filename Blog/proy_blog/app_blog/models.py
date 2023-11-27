from django.db import models
from datetime import datetime
# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=64)
    subtitulo = models.CharField(max_length=64)
    cuerpo = models.CharField(max_length=64)
    autor = models.CharField(max_length=64)
    fecha = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.titulo},{self.fecha}"
    
#class Usuario(models.Model):
    #apellido = models.CharField(max_length=256)
    #nombre = models.CharField(max_length=256)
    #email = models.EmailField(blank=True)
    #telefono = models.CharField(max_length=20, blank=True, null=True)
    #dni = models.CharField(max_length=32)
    #fecha_nacimiento = models.DateField(null=True)
    #creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    #def __str__(self):
        #return f"{self.apellido}, {self.nombre}"