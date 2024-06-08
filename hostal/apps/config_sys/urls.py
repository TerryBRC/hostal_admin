from django.urls import path
from .views import SysConfigCrearLista, SysConfigDetalle

urlpatterns = [
    path('', SysConfigCrearLista.as_view(), name='listar_config'),
    path('<int:pk>/', SysConfigDetalle.as_view(), name='detalle_config'),
]