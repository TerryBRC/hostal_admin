from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','correo_electronico')
    search_fields = ('nombre','apellido',)
    list_filter = ('nombre',)
    date_hierarchy = 'fecha_registro'

admin.site.register(Cliente,ClienteAdmin)