from django.db import models
from django.utils.functional import cached_property

from api.equipo.models import Equipo
from api.cliente.models import Cliente, Direccion

class Orden(models.Model):
    PENDING = "P"
    COMPLETED = "C"

    STATUS_CHOICES = ((PENDING, _("pending")), (COMPLETED, _("completed")))

    comprador = models.ForeignKey(Cliente, related_name="orders", on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    direccion_envio = models.ForeignKey(
        Direccion,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    direccion_pago = models.ForeignKey(
        Direccion,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.buyer.get_full_name()

    @cached_property
    def total_cost(self):
        """
        Total cost of all the items in an order
        """
        return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)


class OrdenItem(models.Model):
    orden = models.ForeignKey(
        Orden, related_name="orden_items", on_delete=models.CASCADE
    )
    equipo = models.ForeignKey(
        Equipo, related_name="equipo_orden", on_delete=models.CASCADE
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
        Total cost of the ordered item
        """
        return round(self.cantidad * self.equipo.precio, 2)