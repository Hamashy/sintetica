from django.db import models
from canchas.models import Cancha

class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    id_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField()
    
    def save(self, *args, **kwargs):
        # Automatically set the cancha to 'Mantenimiento' status
        cancha = self.id_cancha
        cancha.estado = 'MANTENIMIENTO'
        cancha.save()
        super(Mantenimiento, self).save(*args, **kwargs)

    def _str_(self):
        return f'Mantenimiento {self.id_mantenimiento} - {self.fecha}'