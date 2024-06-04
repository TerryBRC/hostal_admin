from django.urls import path
from .views import *

urlpatterns = [
    path('api/habitacion/',HabitacionListarHabitacion.as_view(),name='listar_habitacion'),
    path('api/habitacion/<int:pk>',HabitacionDetalle.as_view(),name='detalle_habitacion')
]
