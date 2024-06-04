from django.db import models
from apps.tipo_habitaciones.models import TipoHabitacion

class Habitacion(models.Model):
    numero_habitacion = models.CharField(max_length=10,verbose_name='Habitación #',null=False,blank=False)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    capacidad_maxima = models.IntegerField(verbose_name='Capacidad Máxima',null=False,blank=False)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Precio por Noche',null=False,blank=False)
    disponible = models.BooleanField(default=True,verbose_name='Disponible')

    class Meta:
        verbose_name_plural = 'Habitaciones'
        db_table= 'habitacion'

    def __str__(self):
        return f'{self.numero_habitacion} - {self.tipo_habitacion}'