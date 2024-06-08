from django.urls import path
from .views import *

urlpatterns = [
    path('',HabitacionCrearLista.as_view(),name='listar_habitacion'),
    path('<int:pk>',HabitacionDetalle.as_view(),name='detalle_habitacion')
]
