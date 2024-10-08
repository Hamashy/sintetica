from django.contrib import admin
from reservas.models import Reserva, ReservaConjunta

# Register your models here.


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    pass

#@admin.register(ReservaConjunta)
#class ReservaConjuntaAdmin(admin.ModelAdmin):
#    pass
