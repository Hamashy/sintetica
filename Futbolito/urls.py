from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#from reservas.api import views
from usuarios.api.router import router_user


from canchas.api.router import router_canchas
from mantenimiento.api.router import router_mantenimiento
from notificaciones.api.router import router_notificaciones
from reservas.api.router import router_reservas, router_reservasconjuntas, router_ReservaUser

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('usuarios.api.router')),
    path('api/', include(router_canchas.urls)),
    path('api/', include(router_mantenimiento.urls)),
    path('api/', include(router_notificaciones.urls)),
    path('api/', include(router_reservas.urls)),
    path('api/', include(router_reservasconjuntas.urls)),
    path('api/', include(router_ReservaUser.urls)),
   #path('generar-pdf/', views.generar_pdf, name='generar_pdf'),


]