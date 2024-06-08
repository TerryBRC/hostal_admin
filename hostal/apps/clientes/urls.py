from django.urls import path
from .views import ClienteCrearLista, ClienteDetalle

urlpatterns = [
    path('', ClienteCrearLista.as_view(), name='listar_clientes'),
    path('<int:pk>/', ClienteDetalle.as_view(), name='detalle_cliente'),
]