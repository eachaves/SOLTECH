
from ..models import Cliente
from ..serializer import ClienteSerializer

def create(cliente: ClienteSerializer) -> Cliente:
    try:
        if cliente.data['is_empresa']:
            raise Exception('You dont have permissions to create an enteprise')
        cliente= Cliente(
            user=cliente.validated_data['user'],
            telefono=cliente.validated_data['telefono'],
            avatar=cliente.validated_data['avatar'],
            bio=cliente.validated_data['bio'],
        )
        cliente.save()
        return cliente
    except Exception as e:
        raise Exception(e.args[0], 500)

    
        
 