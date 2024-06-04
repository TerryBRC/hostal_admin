from django.urls import path
from .views import SysConfigCrearLista, SysConfigDetalle

urlpatterns = [
    path('api/config/', SysConfigCrearLista.as_view(), name='listar_config'),
    path('api/config/<int:pk>/', SysConfigDetalle.as_view(), name='detalle_config'),
]