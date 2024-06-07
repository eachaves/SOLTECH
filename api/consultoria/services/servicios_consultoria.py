from ..serializers import ServicioConsultoriaCreateSerializer
from ..models import ServicioConsultoria

from ...cliente.services import cliente_functions as cliente_crud
from ...empleado.services import crud as empleado_crud
from ...consultoria.services import crud as consultoria_crud

import datetime
def create_servicio(servicio: ServicioConsultoriaCreateSerializer) -> ServicioConsultoria:
    try:
        cliente= cliente_crud.get_cliente_by_id(servicio.data['clienteId'])
        empleado= empleado_crud.get_empleado_by_id(servicio.data['empleadoId'])
        consultoria= consultoria_crud.get_by_id(servicio.data['consultoriaId'])
        servicio = ServicioConsultoria(
            clienteId=cliente,
            empleadoId=empleado,
            consultoriaId=consultoria,
            duracion=servicio.data['duracion'],
        )
        servicio.save()
        return servicio
    except Exception as e:
        raise Exception(e.args[0], 500)

def get_all_servicios() -> list[ServicioConsultoria]:
    try:
        return ServicioConsultoria.objects.all()
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_servicio_by_id(servicio_id: int) -> ServicioConsultoria:
    try:
        if not exists(servicio_id):
            raise Exception('Servicio consultoria not found', 404)
        return ServicioConsultoria.objects.get(id=servicio_id)
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def update_fecha_fin(servicio_id: int) -> ServicioConsultoria:
    try:
        servicio= get_servicio_by_id(servicio_id)
        servicio.fechaFin= datetime.datetime.now()
        servicio.save()
        return servicio
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def exists(servicio_id: int) -> bool:
    try:
        return ServicioConsultoria.objects.filter(id=servicio_id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)