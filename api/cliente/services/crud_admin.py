
from ..models import Cliente, Direccion
from api.authentication.serializer import SignUpSerializer
from api.authentication.services.auth import signup
from api.authentication.models import User


def get_all() -> list[Cliente]:
    try:
        return Cliente.objects.all()
    except Exception as e:
        raise Exception(e.args[0], 500)

def create_by_admin(cliente: SignUpSerializer) -> User:
    try:
        user= signup(cliente)
        
        cliente= Cliente(
            user=user,
            telefono=0,
            avatar="",
            bio="",
            is_empresa=True
        )
        cliente.save()
        return user
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def exists(id:int) -> bool:
    try:
        return Cliente.objects.filter(id=id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)
    
def get_all_direcciones_by_admin() -> list[Direccion]:
    try:
        direcciones= Direccion.objects.all()
        return direcciones
    except Exception as e:
        raise Exception(e.args[0], 500)