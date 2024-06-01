from ..models import Empleado
from ..serializer import EmployeeCreateAdminSerializer, EmployeeCreatedSerializer
from api.authentication.serializer import SignUpSerializer
from api.authentication.services.auth import signup

def create(empleado: EmployeeCreateAdminSerializer) -> EmployeeCreatedSerializer:
    try:
        user_data = SignUpSerializer(
            data={
                'username': empleado.validated_data['username'],
                'first_name': empleado.validated_data['first_name'],
                'last_name': empleado.validated_data['last_name'],
                'email': empleado.validated_data['email'],
                'password': empleado.validated_data['password']
            })
        if not user_data.is_valid():
            raise Exception(user_data.errors, 400)
        user= signup(
            user_data
        )
        empleado = Empleado(
            user = user,
            puesto = empleado.validated_data['puesto'],
            telefono = empleado.validated_data['telefono'],
            fechaContratacion = empleado.validated_data['fechaContratacion']
        )
        empleado.save()
        employee= EmployeeCreatedSerializer(
            data={
                'username': empleado.user.username,
                'first_name': empleado.user.first_name,
                'last_name': empleado.user.last_name,
                'email': empleado.user.email,
                'puesto': empleado.puesto,
                'telefono': empleado.telefono,
                'fechaContratacion': empleado.fechaContratacion
            }
        )
        if not employee.is_valid():
            raise Exception(employee.errors, 400)
        return employee
    except Exception as e:
        raise Exception(e.args[0], 500)
