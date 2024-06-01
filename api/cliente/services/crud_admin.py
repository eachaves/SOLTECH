
from ..models import Cliente
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
    
    
def delete_by_admin(id: int) -> None:
    try:
        if not exists(id):
            raise Exception('Cliente not found')
        cliente= Cliente.objects.get(id=id)
        cliente.delete()
    except Exception as e:
        if e.args[0] == 'Cliente not found':
            raise Exception('Cliente not found', 404)
        raise Exception(e.args[0], 500)
 
def exists(id:int) -> bool:
    try:
        return Cliente.objects.filter(id=id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)