
from ..models import Cliente
from ..serializer import ClienteSerializer
from api.authentication.services.auth import get_user
def create(cliente: ClienteSerializer) -> Cliente:
    try:
        user = get_user(cliente.validated_data['user'])
        cliente= Cliente(
            user=user,
            telefono=cliente.validated_data['telefono'],
            avatar=cliente.validated_data['avatar'],
            bio=cliente.validated_data['bio']
        )
        cliente.save()
        return cliente
    except Exception as e:
        raise Exception(e.args[0], 500)
    
    
        
 