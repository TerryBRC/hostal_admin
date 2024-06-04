from django.urls import path
from .views import *

urlpatterns = [
    path('api/reserva/',ReservaListarCrear.as_view(),name='listar_reservas'),
    path('api/reserva/<int:pk>',ReservaDetalle.as_view(),name='detalle_reserva')
]
