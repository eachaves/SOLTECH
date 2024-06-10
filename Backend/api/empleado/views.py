from .serializer import EmpleadoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.crud import create#, get, update, delete
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_empleado_view(request):
    try:
        empleado = EmpleadoSerializer(data=request.data)
        if not empleado.is_valid():
            print(empleado)
            return Response(empleado.errors, status=status.HTTP_400_BAD_REQUEST)
        empleado = create(empleado)
        return Response(EmpleadoSerializer(empleado).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])