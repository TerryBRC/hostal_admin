from django.urls import path
from .views import *

urlpatterns = [
    path('api/crear/',TipoHabitacionListarCrear.as_view(),name='listar_tipohabitacion'),
    path('api/detalle/<int:pk>',TipoHabitacionDetalle.as_view(),name='detalle_tipohabitacion'),
]
