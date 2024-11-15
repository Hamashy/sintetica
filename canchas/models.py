from django.db import models

ESTADO_CHOICES = [
    ('DISPONIBLE', 'Disponible'),
    ('RESERVADA', 'Reservada'),
    ('MANTENIMIENTO', 'Mantenimiento'),
]

class Cancha(models.Model):
    id_cancha = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100, default='Desconocido')  # Valor por defecto
    precio_por_hora = models.DecimalField(max_digits=6, decimal_places=2 , default=10.00)  # Valor por defecto

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE')  # Estado de la cancha

    def reservar(self):
        """Método para cambiar el estado a Reservada"""
        self.estado = 'RESERVADA'
        self.save()

    def liberar(self):
        """Método para cambiar el estado a Disponible"""
        self.estado = 'DISPONIBLE'
        self.save()

    def __str__(self):
        return f"{self.nombre} - {self.barrio}"

    class Meta:
        verbose_name_plural = "Canchas"
