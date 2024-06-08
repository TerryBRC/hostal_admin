from django.urls import path
from .views import FacturaCearLista, FacturaDetalle

urlpatterns = [
    path('', FacturaCearLista.as_view(), name='listar_facturas'),
    path('<int:pk>/', FacturaDetalle.as_view(), name='detalle_factura'),
]