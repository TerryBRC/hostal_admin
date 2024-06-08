from django.urls import path
from .views import *

urlpatterns = [
    path('',HabitacionListarHabitacion.as_view(),name='listar_habitacion'),
    path('<int:pk>',HabitacionDetalle.as_view(),name='detalle_habitacion')
]
