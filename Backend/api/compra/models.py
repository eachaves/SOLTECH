from django.db import models
from django.utils.functional import cached_property
from api.equipo.models import Equipo
from api.cliente.models import Cliente, Direccion
from django.utils.translation import gettext_lazy as _

class Compra(models.Model):
    PENDING = "P"
    COMPLETED = "C"

    STATUS_CHOICES = ((PENDING, ("pending")), (COMPLETED, _("completed")))

    comprador = models.ForeignKey(Cliente,  on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    direccion_envio = models.ForeignKey(
        Direccion,
        related_name="direccion_envio",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    direccion_pago = models.ForeignKey(
        Direccion,
        related_name="direccion_pago",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )   

    created_at = models.DateTimeField(auto_now_add=True)# is the same date
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.comprador.get_full_name()

    @cached_property
    def total_cost(self):
        """
        Costo total de todos los elementos en una compra
        """
        return round(sum([compra_item.total_cost for compra_item in self.compra_items.all()]), 2)


class CompraItem(models.Model):
    compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, related_name="compra_items"
    )
    equipo = models.ForeignKey(
        Equipo,on_delete=models.CASCADE, related_name="equipo_compra"
    )
    cantidad = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.orden.comprador.get_full_name()

    @cached_property
    def total_cost(self):
        """
        Costo total para un item en una compra,
        un item se refiere a un equipo en una compra
        que puede ser mas de uno
        """
        return round(self.cantidad * self.equipo.precio, 2)