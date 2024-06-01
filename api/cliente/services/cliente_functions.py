
from ..models import Cliente
from ..serializer import ClienteUpdateProfilesSerializer
from api.authentication.serializer import SignUpSerializer
from api.authentication.services.auth import signup
from api.authentication.models import User

def create(cliente: SignUpSerializer) -> User:
    try:
        user= signup(cliente)
        
        cliente= Cliente(
            user=user,
            telefono=0,
            avatar="",
            bio="",
            is_empresa=False
        )
        cliente.save()
        return user
    except Exception as e:
        raise Exception(e.args[0], 500)

def update(cliente: ClienteUpdateProfilesSerializer, user_id: int) -> Cliente:
    try:
        cliente= get_cliente_by_user_id(user_id)
        print('Cliente:', cliente)
        for key, value in cliente.data.items():
            if value is not None:
                setattr(cliente, key, value)
        cliente.save()
        return cliente
    except Exception as e:
        if e.args[0] == 'Cliente not found':
            raise Exception('Cliente not found', 404)
        raise Exception(e.args[0], 500)

def get_cliente_by_user_id(user_id: int) -> Cliente:
    try:
        if not exists_by_user_id(user_id):
            raise Exception('Cliente not found')
        return Cliente.objects.get(user=user_id)
    except Exception as e:
        raise Exception(e.args[0], 500)
        
def exists_by_user_id(user_id: int) -> bool:
    try:
        return Cliente.objects.filter(user=user_id).exists()
    except Exception as e:
        raise Exception(e.args[0], 500)