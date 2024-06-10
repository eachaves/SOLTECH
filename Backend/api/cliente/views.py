from .serializer import ClienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.crud_cliente import create#, get, update, delete
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cliente_view(request):
    try:
        cliente = ClienteSerializer(data=request.data)
        if not cliente.is_valid():
            return Response(cliente.errors, status=status.HTTP_400_BAD_REQUEST)
        cliente = create(cliente)
        return Response(ClienteSerializer(cliente).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])