from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from .serializers import ReservaSerializer
from .models import Reserva


class ReservaListarCrear(generics.ListCreateAPIView):
    model = Reserva.objects.all()
    queryset = ReservaSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class ReservaDetalle(generics.RetrieveUpdateDestroyAPIView):
    model = Reserva.objects.all()
    queryset = ReservaSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]