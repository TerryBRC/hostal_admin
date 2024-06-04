from django.db import models

class TipoHabitacion(models.Model):
    tipo_habitacion = models.CharField(max_length=30,verbose_name='Tipo de Habitación',null=False,blank=False)
    descripcion = models.CharField(max_length=100,verbose_name='Descripción',null=False,blank=False)

    class Meta:
        verbose_name_plural = 'Tipos de Habitaciones'
        db_table= 'tipo_habitacion'

    def __str__(self):
        return f'{self.tipo_habitacion}'
