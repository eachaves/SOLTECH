from .serializer import EmployeeCreateAdminSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.crud_admin import create#, get, update, delete
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