
from ..models import Cliente
from api.authentication.serializer import SignUpSerializer
from api.authentication.services.auth import signup

    
def create(cliente: SignUpSerializer) -> Cliente:
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
        return cliente
    except Exception as e:
        raise Exception(e.args[0], 500)
    
 