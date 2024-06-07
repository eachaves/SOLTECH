from ..models import Empleado

def exists(id: int) -> bool:
    try:
        return Empleado.objects.filter(id=id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_empleado_by_id(id: int) -> Empleado:
    try:
        if not exists(id):
            raise Exception('Empleado not found', 404)
        return Empleado.objects.get(id=id)
    except Exception as e:
        raise Exception(e.args[0], e.args[1])