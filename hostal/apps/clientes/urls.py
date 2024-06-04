from django.urls import path
from .views import ClienteCrearLista, ClienteDetalle

urlpatterns = [
    path('api/cliente/', ClienteCrearLista.as_view(), name='listar_clientes'),
    path('api/cliente/<int:pk>/', ClienteDetalle.as_view(), name='detalle_cliente'),
]