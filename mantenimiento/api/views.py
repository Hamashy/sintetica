from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from mantenimiento.api.serializers import MantenimientoSerializer, MantenimientoCreateSerializer
from mantenimiento.models import Mantenimiento


class MantenimientoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return MantenimientoCreateSerializer  # Usa el serializer sin depth para POST
        return MantenimientoSerializer  # Usa el serializer con depth para GET

    # Mantén el queryset como antes
    queryset = Mantenimiento.objects.select_related('id_cancha').all()