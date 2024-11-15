from django.db import router
from rest_framework.routers import DefaultRouter

from reservas.api.views import ReservaConjuntaApiViewSet, ReservasApiViewSet, ReservaSoloApiViewSet, UserReservasApiView



router_reservas = DefaultRouter()
router_reservasconjuntas = DefaultRouter()
router_ReservaSolo = DefaultRouter()
router_ReservaUser = DefaultRouter()


router_reservas.register(prefix='reservas', basename='reservas', viewset=ReservasApiViewSet)
router_reservasconjuntas.register(prefix='reservasconjuntas', basename='reservasconjuntas', viewset=ReservaConjuntaApiViewSet)
router_ReservaSolo.register(prefix='reservaSolo', basename='reservaSolo', viewset=ReservaSoloApiViewSet)


router_ReservaUser.register(prefix='reservas/user', viewset=UserReservasApiView, basename='user_reservas')