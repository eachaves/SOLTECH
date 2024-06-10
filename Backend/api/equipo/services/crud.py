from ..models import Equipo
from ..serializers import EquipoSerializer, EquipoSerializerUpdate

def create(equipo: EquipoSerializer) -> Equipo:
    try:
        equipo = Equipo(
            nombreEquipo=equipo.data['nombreEquipo'],
            urlImagen=equipo.data['urlImagen'],
            descripcion=equipo.data['descripcion'],
            precio=equipo.data['precio'],
            stock=equipo.data['stock']
        )
        equipo.save()
        return equipo
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_all() -> list:
    try:
        return Equipo.objects.all()
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_by_id(id: int) -> Equipo:
    try:
        if not exists(id):
            raise Exception('Equipo not found')
        return Equipo.objects.get(id=id)
    except Exception as e:
        if e.args[0] == 'Equipo not found':
            raise Exception('Equipo not found', 404)
        raise Exception(e.args[0], 500)
    
def update(equipoData: EquipoSerializerUpdate, id: int) -> Equipo:
    try:
        if not exists(id):
            raise Exception('Equipo not found')
        equipo = get_by_id(id)
        for key, value in equipoData.data.items():
            if value is not None:
                setattr(equipo, key, value)         
        equipo.save()
        return equipo
    except Exception as e:
        if e.args[0] == 'Equipo not found':
            raise Exception('Equipo not found', 404)
        raise Exception(e.args[0], 500)

def delete(id: int) -> None:
    try:
        if not exists(id):
            raise Exception('Equipo not found')
        equipo = get_by_id(id)
        equipo.delete()
    except Exception as e:
        if e.args[0] == 'Equipo not found':
            raise Exception('Equipo not found', 404)
        raise Exception(e.args[0], 500)

def exists(id: int) -> bool:
    try:
        return Equipo.objects.filter(id=id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)
