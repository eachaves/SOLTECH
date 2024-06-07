from ..models import Consultoria
from ..serializers import ConsultoriaSerializer

def create(consultoria: ConsultoriaSerializer) -> Consultoria:
    try:
        consultoria = Consultoria(
            tipoServicio=consultoria.data['tipoServicio'],
            descripcion=consultoria.data['descripcion'],
            precio=consultoria.data['precio'],
        )
        consultoria.save()
        return consultoria
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_all() -> list:
    try:
        return Consultoria.objects.all()
    except Exception as e:
        raise Exception(e.args[0], 500)

def get_by_id(id: int) -> Consultoria:
    try:
        if not exists(id):
            raise Exception('Consultoria not found')
        return Consultoria.objects.get(id=id)
    except Exception as e:
        if e.args[0] == 'Consultoria not found':
            raise Exception('Consultoria not found', 404)
        raise Exception(e.args[0], 500)
    
def delete(id: int) -> None:
    try:
        if not exists(id):
            raise Exception('Consultoria not found')
        consultoria = get_by_id(id)
        consultoria.delete()
    except Exception as e:
        if e.args[0] == 'Consultoria not found':
            raise Exception('Consultoria not found', 404)
        raise Exception(e.args[0], 500)

def exists(id: int) -> bool:
    try:
        return Consultoria.objects.filter(id=id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)