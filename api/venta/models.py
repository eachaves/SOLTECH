from django.db import models
from django.utils.functional import cached_property
from api.equipo.models import Equipo
from api.cliente.models import Cliente, Direccion
from django.utils.translation import gettext_lazy as _
import uuid

class Venta(models.Model):
    PENDING = "P"
    PROCESSING = "PR"
    APPROVED = "A"
    REJECTED = "R"
    FAILED = "F"

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    STATUS_CHOICES = ((PENDING, ("pending")), (PROCESSING, _("processing")), (APPROVED, _("approved")), (REJECTED, _("rejected")), (FAILED, _("failed")))

    comprador = models.ForeignKey(Cliente,  on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    direccion_envio = models.ForeignKey(
        Direccion,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="direccion_envio",
    )
    direccion_pago = models.ForeignKey(
        Direccion,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="direccion_pago",
    )
    divisa = models.CharField(max_length=3, default="COP", editable=False)
    
    created_at = models.DateTimeField(auto_now_add=True)# is the same date
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.comprador.user.get_full_name()

    @cached_property
    def total_cost(self):
        """
        Costo total de todos los elementos en una compra
        """
        return round(sum([venta_item.total_cost for venta_item in self.venta_items.all()]), 2)


class VentaItem(models.Model):
    venta = models.ForeignKey(
        Venta, on_delete=models.CASCADE, related_name="venta_items"
    )
    equipo = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, related_name="equipo_venta"
    )
    cantidad = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.venta.comprador.user.get_full_name()

    @cached_property
    def total_cost(self):
        """
        Costo total para un item en una compra,
        un item se refiere a un equipo en una compra
        que puede ser mas de uno
        """
        return round(self.cantidad * self.equipo.precio, 2)