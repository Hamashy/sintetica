from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mantenimiento.models import Mantenimiento  # Asegúrate de importar tu modelo Consultorio aquí\



class MantenimientoSerializer(ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        depth = 1

class MantenimientoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'  # O puedes listar los campos específicos que deseas permitir