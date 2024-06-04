from django.urls import path
from .views import FacturaCearLista, FacturaDetalle

urlpatterns = [
    path('api/factura/', FacturaCearLista.as_view(), name='listar_facturas'),
    path('api/factura/<int:pk>/', FacturaDetalle.as_view(), name='detalle_factura'),
]