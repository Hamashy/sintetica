from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from reservas.models import Reserva, ReservaConjunta  # Asegúrate de importar tu modelo Consultorio aquí\



class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        depth = 1

class ReservasCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'  # O puedes listar los campos específicos que deseas permitir

class ReservaConjuntaSerializer(ModelSerializer):
    class Meta:
        model = ReservaConjunta
        fields = '__all__'