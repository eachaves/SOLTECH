from api.empresa.models import Empresa
from ..serializers import EmpresaSerializer

def create(empresa: EmpresaSerializer) -> Empresa:
    try:
        empresa = Empresa(
            nombreEmpresa=empresa.data['nombreEmpresa'],
            direccion=empresa.data['direccion'],
            telefono=empresa.data['telefono'],
            email=empresa.data['email']
        )
        empresa.save()
        return empresa
    except Exception as e:
        raise Exception(e.args[0], 500)

def get_all() -> list:
    try:
        empresas = Empresa.objects.all()
        return empresas
    except Exception as e:
        raise Exception(str(e), 500)
    
def get_by_id(id: int) -> Empresa:
    try:
        empresa = Empresa.objects.get(id=id)
        return empresa
    except Exception as e:
        raise Exception(str(e), 500)