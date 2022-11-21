from django.db import models
import time
class Posicion(models.Model):
    titulo = models.CharField(max_length=50);
    
    def __str__(self):
        return self.titulo
class Empleado(models.Model):
    nombre_comp = models.CharField(max_length=100)
    codigo_emp = models.CharField(max_length=3)    
    celular = models.CharField(max_length=15)
    posicion = models.ForeignKey(Posicion,on_delete=models.CASCADE)
    act_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
   
   
