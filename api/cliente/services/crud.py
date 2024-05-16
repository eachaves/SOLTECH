from api.cliente.models import Cliente

def create(data):
    return Clientez.objects.create(**data)