from django.contrib import admin
from .models import SysConfig

class SysConfigAdmin(admin.ModelAdmin):
    list_display = ('clave','valor')
    search_fields = ('clave','valor',)
    list_filter = ('clave',)

admin.site.register(SysConfig,SysConfigAdmin)