from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .serializers import FacturaSerializer
from .models import Factura

class FacturaCearLista(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]


class FacturaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]