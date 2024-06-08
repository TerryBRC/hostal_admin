from django.urls import path
from .views import *

urlpatterns = [
    path('',TipoHabitacionListarCrear.as_view(),name='listar_tipohabitacion'),
    path('<int:pk>',TipoHabitacionDetalle.as_view(),name='detalle_tipohabitacion'),
]
