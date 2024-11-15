from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import HttpResponse
from django.template.loader import render_to_string
#from weasyprint import HTML
#from reservas.models import Reserva 



from reservas.api.serializers import ReservasSerializer, ReservaConjuntaSerializer, ReservasCreateSerializer
from reservas.models import Reserva, ReservaConjunta, ColaSolo

class UserReservasApiView(ModelViewSet):
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        # Filtra las reservas por el usuario especificado en la URL
        user_id = self.kwargs.get('user_id')  # Obtén el user_id de la URL
        return Reserva.objects.filter(id_usuario_id=user_id)

    def list(self, request, user_id=None):
        print(f"Request user: {request.user.id}")
        # Usa get_queryset para obtener las reservas del usuario
        reservas = self.get_queryset()

        if not reservas.exists():
            return Response({"detail": "No Reserva matches the given query."}, status=404)

        serializer = ReservasSerializer(reservas, many=True)
        return Response(serializer.data)

class ReservasApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return ReservasCreateSerializer  # Usa el serializer sin depth para POST y PUT
        return ReservasSerializer  # Usa el serializer con depth para GET

    queryset = Reserva.objects.select_related('id_usuario', 'id_cancha').all()

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def user_reservas(self, request, user_id=None):
        """
        Endpoint para obtener reservas de un usuario específico.
        URL: /api/reservas/user/<user_id>/
        """
        reservas = self.queryset.filter(id_usuario_id=user_id)
        if not reservas.exists():
            return Response({"detail": "No Reserva matches the given query."}, status=404)
        serializer = self.get_serializer(reservas, many=True)
        return Response(serializer.data)

class ReservaConjuntaApiViewSet(ModelViewSet):
    queryset = ReservaConjunta.objects.all()
    serializer_class = ReservaConjuntaSerializer
    permission_classes = [IsAdminUser]

class ReservaSoloApiViewSet(ModelViewSet):
    # Usamos select_related para optimizar la consulta de FK
    queryset = Reserva.objects.select_related('id_usuario', 'id_cancha').all()
    serializer_class = ReservasSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        # Obtén el usuario del request
        usuario = self.request.user

        # Extrae el ID de la cancha desde los datos validados
        cancha_id = self.request.data.get('id_cancha')

        # Asegúrate de que la reserva tenga un id_cancha válido
        if cancha_id is not None:
            # Añade al usuario a la cola
            ColaSolo.objects.create(id_usuario=usuario, id_cancha_id=cancha_id)

            # Verifica si la cola está completa
            if ColaSolo.verificar_equipo_completo(cancha_id):
                anfitrion = ColaSolo.obtener_anfitrion(cancha_id)
                # Notifica a los usuarios
                mensaje = f"El equipo está completo para {anfitrion.id_cancha.nombre}. Esperando a que el anfitrión programe la hora."
                anfitrion.notificar_usuarios(mensaje)

        print(f"Reserva creada con id_cancha: {cancha_id}")


# def generar_pdf(request):
#     # Obtiene todas las reservas (puedes personalizar la consulta)
#     reservas = Reserva.objects.all()
    
#     # Renderiza una plantilla HTML con la información de las reservas
#     html_string = render_to_string('reservas_pdf.html', {'reservas': reservas})
    
#     # Genera el PDF con WeasyPrint
#     pdf_file = HTML(string=html_string).write_pdf()

#     # Devuelve el PDF como una respuesta HTTP
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="reservas.pdf"'
#     return response



def generate_pdf(request):
    # Configurar la respuesta como un PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_reservas.pdf"'

    # Crear el PDF
    pdf = canvas.Canvas(response)
    pdf.drawString(100, 750, "Reporte de Reservas")
    # Agrega más contenido al PDF aquí

    pdf.showPage()
    pdf.save()
    return response