from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.clientes.urls')),
    path('',include('apps.config_sys.urls')),
    path('',include('apps.facturas.urls')),
    path('',include('apps.habitaciones.urls')),
]
