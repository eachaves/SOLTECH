from ..models import Direccion
from ..serializer import DireccionClienteCreateSerializer

def create_direccion(direccionCreate: DireccionClienteCreateSerializer):
    direccion = Direccion(
        cliente_id=direccionCreate.data["cliente"],
        tipo_direcciom=direccionCreate.data["tipo_direccion"],
        pais=direccionCreate.data["pais"],
        ciudad=direccionCreate.data["ciudad"],
        direccion_detalle=direccionCreate.data["direccion_detalle"],
        codigo_postal=direccionCreate.data["codigo_postal"]
    )
    direccion.save()
    return direccion

def get_all_direcciones_shipping(cliente: int):
    try:
        print('Getting all direcciones')
        return Direccion.objects.filter(cliente=cliente, tipo_direcciom=Direccion.SHIPPING)
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_all_direcciones_billing(cliente: int):
    try:
        return Direccion.objects.filter(cliente=cliente, tipo_direcciom=Direccion.BILLING)
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_direccion_by_id(id: int):
    try:
        if not exists(id):
            raise Exception('Direccion not found', 404)
        return Direccion.objects.get(id=id)
    except Exception as e:
        raise Exception(e.args[0], 500)

def exists(id: int) -> bool:
    try:
        return Direccion.objects.filter(id=id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)