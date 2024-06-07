from ..models import Venta, VentaItem
from ..serializer import VentaItemSerializer, VentaCreateSerializer
from ..services.crud_item_venta import create_venta_item
from ...cliente.services.cliente_functions import get_cliente_by_id
from ...cliente.services.crud_direccion import get_direccion_by_id

def create(venta: VentaCreateSerializer):
    try:
        cliente=get_cliente_by_id(venta.data['comprador'])
        direccion_envio=get_direccion_by_id(venta.data['direccion_envio'])
        direccion_pago=get_direccion_by_id(venta.data['direccion_pago'])
        ventaObj = Venta(
            comprador=cliente,
            estado=venta.data['estado'],
            direccion_envio=direccion_envio,
            direccion_pago=direccion_pago
        )
        ventaObj.save()
        for item in venta.data['equipos']:
            create_venta_item(item, ventaObj)
        return ventaObj
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_all():
    try:
        return Venta.objects.all()
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_by_id(id: int):
    try:
        if not exists(id):
            raise Exception('Venta not found')
        return Venta.objects.get(id=id)
    except Exception as e:
        if e.args[0] == 'Venta not found':
            raise Exception('Venta not found', 404)
        raise Exception(e.args[0], 500)
    
def exists(id: int) -> bool:
    try:
        return Venta.objects.filter(id=id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)