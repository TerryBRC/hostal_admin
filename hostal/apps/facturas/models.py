from django.db import models
from apps.reservas.models import Reserva
from apps.habitaciones.models import Habitacion
from django.contrib.auth.models import User


class Tipo_Cobro(models.Model):
    tipo_cobro = models.CharField(max_length=50,null=False,blank=False)
    descripcion = models.TextField(null=True)

    class Meta:
        verbose_name = "Tipo de Cobro"
        verbose_name_plural = "Tipos de Cobros"
        db_table = 'tipo_cobro'

    def __str__(self):
        return self.tipo_cobro

class Factura(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True,null=True,verbose_name='Fecha de Emisión')
    total_dias = models.FloatField(verbose_name='Días Totales',default=1)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2,null=True,default=50000)
    fecha_pago = models.DateField(null=True,blank=True)
    detalle_servicios = models.TextField(blank=False,null=False)
    tipo_cobro = models.ForeignKey(Tipo_Cobro, verbose_name='Tipo de Cobro', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, verbose_name='Facturador', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        db_table = 'factura'

    def __str__(self):
        return self.reserva
    