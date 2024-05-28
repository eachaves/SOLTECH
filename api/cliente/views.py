from .serializer import ClienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.cliente_functions import create
from .services.crud_admin import create as create_by_admin
from api.authentication.serializer import SignUpSerializer
from api.authentication.services.auth import get_user
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_client_view(request):
    try:
        cliente = ClienteSerializer(data=request.data)
        if not cliente.is_valid():
            return Response(cliente.errors, status=status.HTTP_400_BAD_REQUEST)
        cliente = create(cliente)
        return Response(ClienteSerializer(cliente).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_client_admin_view(request):
    try:
        admin= get_user(request.user)
        print(admin)
        if not admin.is_superuser:
            print('Is not superuser')
            raise Exception('You do not have permission to create a client', 403)
        cliente = SignUpSerializer(data=request.data)
        if not cliente.is_valid():
            return Response(cliente.errors, status=status.HTTP_400_BAD_REQUEST)
        cliente = create_by_admin(cliente)
        return Response(ClienteSerializer(cliente).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])