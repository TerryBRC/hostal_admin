from django.contrib import admin
from .models import Habitacion


class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero_habitacion','tipo_habitacion','capacidad_maxima','precio_por_noche','disponible')
    search_fields = ('numero_habitacion','tipo_habitacion',)
    list_filter = ('disponible',)

admin.site.register(Habitacion,HabitacionAdmin)