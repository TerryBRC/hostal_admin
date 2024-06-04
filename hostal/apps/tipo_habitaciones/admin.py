from django.contrib import admin
from .models import TipoHabitacion

class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('tipo_habitacion','descripcion')
    search_fields = ('tipo_habitacion',)
    list_filter = ('tipo_habitacion',)


admin.site.register(TipoHabitacion,TipoHabitacionAdmin)