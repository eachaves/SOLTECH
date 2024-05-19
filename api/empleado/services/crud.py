from ..models import Empleado
from ..serializer import EmpleadoSerializer
from api.authentication.services.auth import get_user_by_id

def create(empleado: EmpleadoSerializer) -> Empleado:
    try:
        empleado = Empleado(
            user = empleado.validated_data['user'],
            puesto = empleado.validated_data['puesto'],
            telefono = empleado.validated_data['telefono'],
            fechaContratacion = empleado.validated_data['fechaContratacion']
        )
        empleado.save()
        return empleado
    except Exception as e:
        raise Exception(e.args[0], 500)
