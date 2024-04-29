from django.db import models
from ..cliente.models import Cliente

# Create your models here.
class Compra (models.Model):
    fechaCompra = models.DateField()
    totalCompra = models.IntegerField() #De pronto flotante o decimal se puede también
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class CompraDetalle (models.Model):
    cantidad = models.IntegerField()
    precioUnitario = models.IntegerField() #De pronto flotante o decimal se puede también
    subTotal = models.IntegerField() #De pronto flotante o decimal se puede también
    #equipoId = INVOCAR LLAVE FORANEA
    #compraId = INVOCAR LLAVE FORANEA