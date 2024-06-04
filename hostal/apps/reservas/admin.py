from django.contrib import admin
from .models import Reserva


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente','habitacion','fecha_entrada','fecha_salida','estado_reserva')
    search_fields = ('cliente','habitacion',)
    list_filter = ('estado_reserva',)
    date_hierarchy = 'fecha_entrada'

admin.site.register(Reserva,ReservaAdmin)