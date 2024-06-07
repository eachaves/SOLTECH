from ..models import Venta
from ..services.crud import get_by_id

from ..serializer import VentaSerializer, VentaWithItemsSerializer, VentaItemSerializer

def total_cost(venta_id:int):
    try:
        venta = get_by_id(venta_id)
        return venta.total_cost
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def ventas_cliente(cliente_id: int) -> list[VentaWithItemsSerializer]:
    try:
        ventas = get_ventas_cliente(cliente_id)
        lista = []
        for venta in ventas:
            items = []
            for item in venta.venta_items.all():
                new_item = VentaItemSerializer(
                    data={
                        'equipo': item.equipo.id,
                        'cantidad': item.cantidad
                    }
                )
                if not new_item.is_valid():
                    raise Exception(new_item.errors, 400)
                items.append(new_item.validated_data)
            data = VentaWithItemsSerializer(
                data={
                    'comprador': venta.comprador.id,
                    'estado': venta.estado,
                    'divisa': venta.divisa,
                    'created_at': venta.created_at,
                    'equipos': items,
                    'total_cost': venta.total_cost
                }
            )
            if not data.is_valid():
                raise Exception(data.errors, 400)
            lista.append(data.validated_data)
        return lista
    except Exception as e:
        raise Exception(e.args[0], 500)


def get_ventas_cliente(cliente_id: int) -> list[Venta]:
    try:
        ventas= Venta.objects.filter(comprador=cliente_id)
        return ventas
    except Exception as e:
        raise Exception(e.args[0], 500)