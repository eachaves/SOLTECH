from rest_framework import serializers
from .models import ServicioConsultoria, Consultoria

class ConsultoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultoria
        fields = '__all__'

class ServicioConsultoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioConsultoria
        fields = '__all__'

class ServicioConsultoriaCreateSerializer(serializers.Serializer):
    clienteId = serializers.IntegerField()
    empleadoId = serializers.IntegerField()
    consultoriaId = serializers.IntegerField()
    duracion = serializers.IntegerField()# la duracion esta dada en semanas
        
    