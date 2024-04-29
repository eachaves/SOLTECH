from django.db import models
from ..cliente.models import Cliente
# Create your models here.
class ServicioConsultoria (models.Model):
    tipoServicio = models.CharField(max_length=30) #Hacer listado de opciones de servicios
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField() #De pronto flotante o decimal se puede también
    duracion = models.IntegerField()
    #fechaInicio = FECHA DATE
    #fechaFin = FECHA DATE
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
