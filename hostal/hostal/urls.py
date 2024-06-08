from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/clientes/', include('apps.clientes.urls')),
    path('api/configuraciones/', include('apps.config_sys.urls')),
    path('api/facturas/', include('apps.facturas.urls')),
    path('api/habitaciones/', include('apps.habitaciones.urls')),
    path('api/tipohabitaciones/', include('apps.tipo_habitaciones.urls')),
    path('docs/', include_docs_urls(title='Hostal API')),
]