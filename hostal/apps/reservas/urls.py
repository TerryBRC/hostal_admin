from django.urls import path
from .views import *

urlpatterns = [
    path('',ReservaListarCrear.as_view(),name='listar_reservas'),
    path('<int:pk>',ReservaDetalle.as_view(),name='detalle_reserva')
]
