from django.contrib import admin
from .models import Factura

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('reserva','fecha_emision', 'fecha_pago', 'monto_total')
    list_filter = ('fecha_emision', 'tipo_cobro')
    search_fields =('reserva','fecha_emision')
    date_hierarchy = 'fecha_emision'

admin.site.register(Factura,FacturaAdmin)