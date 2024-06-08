from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hostal API",
        default_version='v1',
        description="Documentación de la API del sistema de reservas del hostal",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@hostal.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/clientes/', include('apps.clientes.urls')),
    path('api/configuraciones/', include('apps.config_sys.urls')),
    path('api/facturas/', include('apps.facturas.urls')),
    path('api/habitaciones/', include('apps.habitaciones.urls')),
    path('api/tipohabitaciones/', include('apps.tipo_habitaciones.urls')),
    path('api/reservas/', include('apps.reservas.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]