from .serializer import EmployeeCreateAdminSerializer, EmpleadoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.crud_admin import *
from .services.crud import *
from .services.servicios_consultorias import *
from rest_framework.permissions import IsAuthenticated
from api.authentication.services.auth import get_user

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_empleado_view(request):
    try:
        admin= get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to create a employee', 403)
        empleado = EmployeeCreateAdminSerializer(data=request.data)
        if not empleado.is_valid():
            return Response(empleado.errors, status=status.HTTP_400_BAD_REQUEST)
        empleado = create(empleado)
        return Response(empleado.data, status=status.HTTP_201_CREATED)
            
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_empleados_view(request):
    try:
        admin= get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to access to obtain all employees', 403)
        empleados = get_all()
        return Response(EmpleadoSerializer(empleados, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def mark_servicio_as_done_view(request, empleado_id, id):
    try:
        current= get_user(request.user)
        if not current.id!= get_empleado_by_id(empleado_id).user.id:
            raise Exception('You do not have permission to mark a servicio consultoria as done', 403)
        mark_as_done(id)
        return Response({'message': 'Servicio consultoria marked successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])