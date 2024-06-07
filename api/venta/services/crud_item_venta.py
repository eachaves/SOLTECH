from ..models import VentaItem, Venta
from ..serializer import VentaItemSerializer
from ...equipo.services.crud import get_by_id

def create_venta_item(item:dict,venta: Venta) -> VentaItem:
    try:
        equipo = get_by_id(item['equipo'])
        item = VentaItem.objects.create(
            venta=venta,
            equipo=equipo,
            cantidad=item['cantidad']  
        )
        return item
    except Exception as e:
        raise Exception(e.args[0], 500)